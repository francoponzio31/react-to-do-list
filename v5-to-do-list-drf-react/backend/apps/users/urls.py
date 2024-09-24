from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListUsersView.as_view(), name="list-users"),
    path("<int:user_id>/", views.UserDetailView.as_view(), name="user-detail"),
    path("current/", views.CurrentUserDetailView.as_view(), name="current-user-detail"),
]
