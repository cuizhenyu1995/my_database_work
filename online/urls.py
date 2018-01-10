from django.conf.urls import patterns, url
from online import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_success/$', views.regist_success, name='regist_success'),
    url(r'^index/grzl/$', views.grzl, name='grzl'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/logout/$', views.logout, name='logout'),
    url(r'^index/about/$', views.about, name='about'),

    url(r'^index/yhgl/$', views.yhgl, name='yhgl'),
    url(r'^index/get_user/$', views.get_user, name='get_user'),
    url(r'^index/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^index/edit_user/$', views.edit_user, name='edit_user'),
    url(r'^index/add_user/$', views.add_user, name='add_user'),

    url(r'^index/get_me/$', views.get_me, name='get_me'),
    url(r'^index/edit_me/$', views.edit_me, name='edit_me'),

    url(r'^index/get_user/$', views.get_user, name='get_user'),
    url(r'^index/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^index/edit_user/$', views.edit_user, name='edit_user'),
    url(r'^index/add_user/$', views.add_user, name='add_user'),

    url(r'^index/tjsb/$', views.tjsb, name='tjsb'),
    url(r'^index/get_device/$', views.get_device, name='get_device'),
    url(r'^index/delete_device/$', views.delete_device, name='delete_device'),
    url(r'^index/edit_device/$', views.edit_device, name='edit_device'),
    url(r'^index/add_device/$', views.add_device, name='add_device'),

    url(r'^index/gmsb/$', views.gmsb, name='gmsb'),
    url(r'^index/get_gmsb/$', views.get_gmsb, name='get_gmsb'),
    # url(r'^index/delete_gmsb/$', views.delete_gmsb, name='delete_gmsb'),
    url(r'^index/edit_gmsb/$', views.edit_gmsb, name='edit_gmsb'),
    url(r'^index/add_gmsb/$', views.add_gmsb, name='add_gmsb'),

    url(r'^index/jcsb/$', views.jcsb, name='jcsb'),
    url(r'^index/get_jcsb/$', views.get_jcsb, name='get_jcsb'),
    # url(r'^index/delete_gmsb/$', views.delete_gmsb, name='delete_gmsb'),
    url(r'^index/edit_jcsb/$', views.edit_jcsb, name='edit_jcsb'),
    url(r'^index/add_jcsb/$', views.add_jcsb, name='add_jcsb'),

    url(r'^index/sbbx/$', views.sbbx, name='sbbx'),
    url(r'^index/get_sbbx/$', views.get_sbbx, name='get_sbbx'),
    # url(r'^index/delete_gmsb/$', views.delete_gmsb, name='delete_gmsb'),
    url(r'^index/edit_sbbx/$', views.edit_sbbx, name='edit_sbbx'),
    url(r'^index/add_sbbx/$', views.add_sbbx, name='add_sbbx'),
)