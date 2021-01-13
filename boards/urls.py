from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path("boards/<int:board_id>/", views.board_topics, name="board_topics"),
    path("boards/<int:board_id>/new/", views.new_topic, name="new_topic"),
    #path("posts/<int:topic_id>/new/", views.new_post, name="new_post")
]
