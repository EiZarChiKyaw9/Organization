from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>',views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>',views.uncross, name='uncross'),
    path('edit/<list_id>',views.edit, name='edit'),
    path('authenticate/logon',views.logon, name='logon'),
    path('authenticate/logout', views.logout_user, name='logout'),
    path('work_volume/work_volume',views.work_volume, name='work_volume'),
    path('slab_level/slab_level',views.slab_level, name='slab_level'),
    path('site/site',views.site, name='site'),
    path('site_info_create/site_info_create',views.wv_main, name='site_info_create'),
    path('wv_main/submit_work_volume',views.submit_work_volume, name='submit_work_volume'),
    path('daily_wv_submission/wv_daily_submission/<site_id>',views.daily_wv_submission, name='wv_daily_submission'),
    path('rp_work_volume/work_volume_report',views.rp_work_volume, name='work_volume_report'),
    path('export_report_csv/report_csv',views.export_report_csv, name='report_csv'),
    ]