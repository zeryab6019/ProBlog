from django.urls import path
from appBlog import views

urlpatterns = [
    path('',views.PostListView.as_view(), name = 'post_list_h'),
    path('about/',views.AboutView.as_view(), name = 'about_h'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail_h'),
    path('post/new',views.CreatePostView.as_view(),name = 'post_new_h'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(), name = 'post_edit_h'),
    path('post/<int:pk>/remove/',views.PostDelete.as_view(), name = 'post_remove_h'),
    path('drafts/',views.DraftListView.as_view(), name = 'post_draft_list_h'),
    path('post/<int:pk>/comment/',views.add_comment_to_post, name = 'add_comment_to_post_h'),
    path('comment<int:pk>/approve/',views.comment_approve, name = 'comment_approve_h'),
    path('comment/<int:pk>/remove/',views.comment_remove, name = 'comment_remove_h'),
    path('post/<int:pk>/publish/',views.post_publish, name = 'post_publish_h'),
]
