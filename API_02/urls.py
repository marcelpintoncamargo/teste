from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.api_overview_function , name = "api_overview_name"),
    path('post_list_path/', views.post_list_function , name = "post_list_name"),
    path('post_create_path/', views.post_create_function , name = "post_create_name"),


    path('post_detail_path/<str:pk>/', views.post_detail_function , name = "post_detail_name"),
    path('post_update_path/<str:pk>/', views.post_update_function , name = "post_update_name"),
    path('post_delete_path/<str:pk>/', views.post_delete_function , name = "post_delete_name"),

]