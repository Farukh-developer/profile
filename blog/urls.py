from django.urls import path
from .views import LoginView, RegisterView, ProfileView, EditProfileView, student, create, update, read, delete

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
   
    path('student/', student, name='student'),
    path('create/', create, name='create'),

    path('read/<int:id>/', read, name='read'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),

    
    
    
    
    
]