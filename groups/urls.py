from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("groups/", views.GroupListView.as_view(), name="group-list"),
    path('groups/new/', views.GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detail'),
    path('groups/<int:pk>/edit/', views.GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group-delete'),
]
