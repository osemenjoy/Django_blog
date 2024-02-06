from django.urls  import path
from .views import HomePage, PostDetails

urlpatterns = [
    path('', HomePage.as_view(), name= 'home'),
    path('post/<int:pk>/', PostDetails.as_view(), name= 'post_detail'),
]