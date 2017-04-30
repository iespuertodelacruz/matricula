from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^m/(?P<edulevel_code>.*)/$", views.student, name="student"),
]
