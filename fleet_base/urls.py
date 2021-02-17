from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'fleet'

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login),
    url(r'^$', views.home, name='index'),
    url(r'^select-sigup/$', views.select, name='select'),
    url(r'^owner-signup/$', views.ownerSignup, name='owner-signup'),
    url(r'^sacco-signup/$', views.saccoSignup, name='sacco-signup'),
    url(r'^sup-signup/$', views.supSignup, name='sup-signup'),
    url(r'^user-logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^loginViews/$', views.loginViews, name='loginViews'),
    
]
