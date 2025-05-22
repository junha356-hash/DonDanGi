from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list_create),
    path('articles/<int:article_id>/', views.article_detail),
    path('articles/<int:article_id>/comments/', views.article_comment_list_create),
    path('articles/<int:article_id>/comments/<int:comment_id>/', views.article_comment_detail_update_delete),
]