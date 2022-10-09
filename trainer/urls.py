from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.log_out, name='log_out'),
    path('home/', views.home, name = 'home'), 
    path("create_trainer/", views.createTrainer, name="create_trainer"),
    path("delete/<int:id>", views.delete_trainer, name="delete_trainer"),
    path("edit/<int:id>", views.edit_trainer, name="edit_trainer"),
]
