"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'unit_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    path('trackers/<str:group>', views.trackers, name='trackers'),
    path('trackers/<str:group>/<int:tracker_id>', views.tracker_show, name='tracker_show'),
    path('trackers/<str:group>/new', views.new_tracker, name='new_tracker'),


    path('trackers/<str:group>/<int:tracker_id>/delete', views.delete_tracker, name='delete_tracker'),
    path('trackers/<str:group>/<int:tracker_id>/entries/new', views.new_tracker_entry, name='new_tracker_entry'),
    path('trackers/<str:group>/<int:tracker_id>/entries/<int:entry_id>', views.edit_tracker_entry, name='edit_tracker_entry'),
    path('trackers/<str:group>/<int:tracker_id>/entries/<int:entry_id>/delete', views.delete_tracker_entry, name='delete_tracker_entry'),

    path('trackers_in_repair/', views.trackers_in_repair, name='trackers_in_repair'),
    path('sticks_missing/', views.sticks_missing, name='sticks_missing'),

    path('trackers/<str:group>/<int:tracker_id>/failures', views.tracker_failures, name='tracker_failures'),
    path('trackers/<str:group>/<int:tracker_id>/failures/new', views.new_tracker_failure, name='new_tracker_failure'),
    path('trackers/<str:group>/<int:tracker_id>/failures/<int:failure_id>/edit', views.edit_tracker_failure, name='edit_tracker_failure'),
    path('trackers/<str:group>/<int:tracker_id>/failures/<int:failure_id>/delete', views.delete_tracker_failure, name='delete_tracker_failure')
]
