from Adminapp import views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
  
    re_path(r'^employee/$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^SaveFile$', views.SaveFile)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

