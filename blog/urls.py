from django.urls import path
from . import views


urlpatterns = [
     path("", views.home, name='home'),
     path("add", views.add_post, name='add-post'),
     path("<int:pk>", views.update_post, name='update-post'),
     path("<int:pk>/", views.post_detail, name='post-detail')

]