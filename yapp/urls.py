from django.urls import path 
from .views import HomePage, DetailPage, DeletePost, RegisterUser, LoginUser, logout_user, add_page, search_post


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('post/<int:pk>/', DetailPage.as_view(), name='detail'),
    path('add/', add_page, name='add'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='del'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/search/', search_post, name='search_post')
]