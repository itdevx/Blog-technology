from django.urls import path
from .views import SignUpBlogView, DashboardBlogView, SignInBlogView, SignOutBlogView, CreateArticle, UpdateArticle, DeleteArticle, UpdateProfile

app_name = 'account'


urlpatterns = [
    path(
        'sign-up/', SignUpBlogView.as_view(), name='sign-up'
    ),
    path(
        'dashboard/', DashboardBlogView.as_view(), name='dashboard'
    ),
    path(
        'sign-in/', SignInBlogView.as_view(), name='sign-in'
    ),
    path(
        'sign-out/', SignOutBlogView.as_view(), name='sign-out'
    ),
    path(
        'dashboard/create-article/', CreateArticle.as_view(), name='create-article'
    ),
    path(
        'dashboard/update-article/<int:pk>/', UpdateArticle.as_view(), name='update-article'
    ),
    path(
        'dashboard/delete-article/<pk>/', DeleteArticle.as_view(), name='delete-article'
    ),
    path(
        'dashboard/update-profile/<int:pk>', UpdateProfile.as_view(), name='update-profile'
    )
]