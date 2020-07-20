from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.welcome, name = 'welcome'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^register/', views.register, name='register'),
    url(r'^create_profile/', views.create_profile, name='create_profile'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^notices/', views.notices, name='notices'),
    url(r'^establishment/', views.establishment, name='establishment'),
    url(r'^post_business/', views.post_business, name='post_business'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)