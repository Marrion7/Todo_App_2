from  django.urls import path
from . import views

urlpatterns = [
    path('', views.ListlViews, name= 'tasks'),
    path('task/<int:id>/', views.Detailview, name='task'),
    path('task-create', views.Createview, name = 'task-create'),
    path('task-update/<int:pk>/', views.Updateview, name= 'task-update'),
    path('task-delete/<int:pk>/', views.Delete, name='task-delete')
    
]