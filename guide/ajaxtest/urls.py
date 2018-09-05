from django.urls import path

from . import views

app_name = 'ajaxtest'
urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book_create/', views.book_create, name='book_create'),
    path('book_update/<pk>/', views.book_update, name='book_update'),
    path('book_delete/<pk>/', views.book_delete, name='book_delete'),
    # path('<pk>/new/', views.new_topic, name='new_topic'),
    # path('<pk>/topics/<topic_pk>/', views.topic_posts, name='topic_posts'),
    # path('<pk>)/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    # path('<pk>/topics/<topic_pk>/posts/<post_pk>/edit/',
    #     views.PostUpdateView.as_view(), name='edit_post'),

]
