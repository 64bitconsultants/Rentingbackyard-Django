__author__ = 'h_hack'
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^signup/$', views.signupview, name='signup'),
    url(r'^logout/$', views.logoutview, name='logout'),
    url(r'^proposal/$', views.proposalview, name='proposal'),

]