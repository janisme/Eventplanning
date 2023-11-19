from django.urls import path
from . import views #. current director

#url config
urlpatterns = [
    path('', views.list, name = 'home'),
    path('view/<int:event_id>/', views.view,name='event_id'),
    path('view/<event_id>/edit/', views.edit,name='event_id'),
    path('view/<event_id>/delete/', views.delete,name='event_id'),
    path('create/', views.create)
]