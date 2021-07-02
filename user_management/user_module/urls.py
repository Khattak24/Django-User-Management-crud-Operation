from django.urls import path
from user_module import views

urlpatterns = [
    path("",views.ListArticleAPIView.as_view(),name="Article_list"),
    path("create/", views.CreateArticleAPIView.as_view(),name="Article_create"),
    path("update/<int:pk>/",views.UpdateArticleAPIView.as_view(),name="update_Article"),
    path("delete/<int:pk>/",views.DeleteArticleAPIView.as_view(),name="delete_Article")
]