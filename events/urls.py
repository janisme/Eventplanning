from django.urls import path
from . import views #. current director

#url config
urlpatterns = [
    path('', views.list, name = 'home'),
    path('view/<int:event_id>/', views.view,name='event_id'),
    path('view/<event_id>/edit/', views.edit_event,name='edit_event'),
    path('view/<event_id>/delete/', views.delete,name='delete_event'),
    path('create/', views.create)
]