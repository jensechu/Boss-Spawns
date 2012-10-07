from datetime import datetime, timedelta
from pytz import timezone
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.models import User
from bossspawns.deathclock.models import Boss, Zone, Server, DeathCount

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
        
