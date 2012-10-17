function escape_from_iframe_trap()
{
    if (top.location != location) {
        top.location.href = document.location.href ;
    }
}

$(document).ready(function(){
    escape_from_iframe_trap();
    $(".errorlist li").addClass("alert-error").addClass("alert");
});


