from django.urls import path
from . import views as appointment_views

urlpatterns = [
    path('appointments/', appointment_views.appointments, name='appointments'),
    path('appointments/<int:appointment_id>/edit/', appointment_views.appointment_edit, name='appointments_edit'),
    path('appointments/<int:appointment_id>/cancel/', appointment_views.cancel_appointment, name='appointments_cancel'),
]
