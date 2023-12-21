from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete_task/<int:task_id>/', views.delete_task_view, name='delete_task')

]