from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.welcome, name = 'welcome'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^register/', views.register, name='register'),
    url(r'^create_profile/', views.create_profile, name='create_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)