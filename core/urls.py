from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r"^$",
        views.index,
        name="index"
    ),
    url(
        r"^m/(?P<edulevel_code>[\dA-Z]+)/$",
        views.student,
        name="student"
    ),
    url(
        r"^m/(?P<edulevel_code>[\dA-Z]+)/academic/$",
        views.academic,
        name="academic"
    ),
]
