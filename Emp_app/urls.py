# from django.conf.urls import re_path
from django.urls import re_path
from Emp_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^empleave/$',views.leaveApi),
    re_path(r'^empleave/([0-9]+)$',views.leaveApi),
]