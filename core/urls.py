from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r"^$",
        views.index,
        name="index"
    ),
    url(
        r"^m/(?P<edulevel_code>[\da-zA-Z]+)/$",
        views.student,
        name="student"
    ),
    url(
        r"^m/(?P<edulevel_code>[\da-zA-Z]+)/academic/$",
        views.academic,
        name="academic"
    ),
    url(
        r"^m/(?P<edulevel_code>[\da-zA-Z]+)/academic/"
        "(?P<itinerary_code>[A-Z]+)/$",
        views.itinerary,
        name="itinerary"
    ),
]
