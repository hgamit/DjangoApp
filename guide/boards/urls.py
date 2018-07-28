from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.home, name='home'),
    path('<pk>/', views.board_topics, name='board_topics'),
    path('<pk>/new/', views.new_topic, name='new_topic'),
    path('<pk>/topics/<topic_pk>/', views.topic_posts, name='topic_posts'),
    path('<pk>)/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('<pk>/topics/<topic_pk>/posts/<post_pk>/edit/',
        views.PostUpdateView.as_view(), name='edit_post'),

]
