from datetime import datetime, timedelta
from pytz import timezone
from django.utils.timezone import now
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
from bossspawns.deathclock.models import Boss, Zone, Server, DeathCount
from bossspawns.deathclock.forms import DeathCountForm

## A timezone object parsed from the timezone
## name set in django.conf.settings
TZ = timezone(settings.TIME_ZONE)

class BossTest(TestCase):
    longMessage = True

    def setUp(self):
        self.server = Server.objects.create(name="Jade Quarry", tz=settings.TIME_ZONE)
        self.zone = Zone.objects.create(name="Sparkfly Fen")
        self.boss = Boss.objects.create(name="Tequatl", respawn_rate=10800, zone=self.zone)

        self.user = User.objects.create_user("jensen")
        self.boss_with_data = Boss.objects.create(name="The Shatterer", respawn_rate=15800, zone=self.zone)

        now = TZ.localize(datetime.now())
        self.death_time = DeathCount.objects.create(
            boss=self.boss_with_data,
            died_at=now,
            server=self.server,
            user=self.user
        )

        self.old_boss_with_data = Boss.objects.create(name="The Slava", respawn_rate=15800, zone=self.zone)

        now = TZ.localize(datetime.now())
        past = timedelta(days=31)
        self.death_time = DeathCount.objects.create(
            boss=self.old_boss_with_data,
            died_at=now - past,
            server=self.server,
            user=self.user
        )

    def test_have_boss(self):
        count = Boss.objects.count()
        self.assertGreater(count, 0, 'No bosses found')

    def test_next_spawn_unknown(self):
        self.assertIsNone(self.boss.next_spawn(self.server), 'Boss should not have spawn time')

    def test_next_spawn_known(self):
        self.assertIsNotNone(self.boss_with_data.next_spawn(self.server), 'Boss should have a spawn time')

    def test_next_spawn_not_in_past(self):
        self.assertIsNone(self.old_boss_with_data.next_spawn(self.server), 'Spawn time would be in the past.')

    def test_next_spawn_is_in_future(self):
        now = TZ.localize(datetime.now())
        self.assertGreater(self.boss_with_data.next_spawn(self.server), now, 'Spawn time should be in the future.')

class DeathFormTest(TestCase):
    longMessage = True
    def setUp(self):
        self.data = {'death_time': '2012-10-07 16:56:38'}
        self.user = User.objects.create_user("jensen")
        self.server = Server.objects.create(name="Jade Quarry", tz=settings.TIME_ZONE)
        self.zone = Zone.objects.create(name="Sparkfly Fen")
        self.boss = Boss.objects.create(name="Tequatl", respawn_rate=10800, zone=self.zone)

    def test_form_save(self):
        form = DeathCountForm(self.data)
        data = form.save(self.user, self.boss, self.server)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, DeathCount)

    def test_matching_submittions_dont_dupe(self):
        # Submit once
        form = DeathCountForm(self.data)
        data = form.save(self.user, self.boss, self.server)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, DeathCount)

        # SUbmit twice
        form = DeathCountForm(self.data)
        data = form.save(self.user, self.boss, self.server)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, DeathCount)

        self.assertEqual(DeathCount.objects.count(), 1, "Second matching submission should not create DeathCount")


class DeathCountTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("jensen")
        self.server = Server.objects.create(name="Jade Quarry", tz=settings.TIME_ZONE)
        self.zone = Zone.objects.create(name="Sparkfly Fen")
        self.boss = Boss.objects.create(name="Tequatl", respawn_rate=10800, zone=self.zone)

        self.death_time = DeathCount.objects.create(
            boss=self.boss,
            died_at=now(),
            server=self.server,
            user=self.user
        )
        self.old_death_time = DeathCount.objects.create(
            boss=self.boss,
            died_at=now() - timedelta(days=30),
            server=self.server,
            user=self.user
        )

    def test_range_search_finds_only_recent_deaths(self):
        deaths = DeathCount.objects.in_spawn_range(self.boss, self.server)
        all_deaths = DeathCount.objects.all()

        self.assertGreater(len(deaths), 0, 'Some death counts should have been found.')
        self.assertLess(len(deaths), len(all_deaths), 'There are too many death times.')
        self.assertEqual(self.death_time.pk, deaths[0].pk, 'Did not find the correct death time.')
