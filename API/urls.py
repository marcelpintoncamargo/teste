from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview_function , name = "api_overview_name"),
    path('task_list_path/', views.task_list_function , name = "task_list_name"),
    path('task_create_path/', views.task_create_function , name = "task_create_name"),


    path('task_detail_path/<str:pk>/', views.task_detail_function , name = "task_detail_name"),
    path('task_update_path/<str:pk>/', views.task_update_function , name = "task_update_name"),
    path('task_delete_path/<str:pk>/', views.task_delete_function , name = "task_delete_name"),

]