from django.urls  import path
from .views import HomePage, PostDetails, CreatePost,EditPost, DeletePost

urlpatterns = [
    path('', HomePage.as_view(), name= 'home'),
    path('post/<int:pk>/', PostDetails.as_view(), name= 'post_detail'),
    path('post/new/', CreatePost.as_view(), name='new_post'),
    path('post/<int:pk>/edits', EditPost.as_view(), name= 'edit_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name= 'delete_post')
]