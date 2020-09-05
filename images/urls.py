from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.image_upload, name='upload_image'),
    path('image_detail/<int:id>/', views.image_detail, name='image_detail'),
    path('image_list/', views.ImageListView.as_view(), name='images_list'),
]
