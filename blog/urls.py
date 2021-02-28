from django.urls import path
from .views import HomeView, ArticleDetailView,\
    AddPostView, UpdatePostView, DeletePostView, \
    AddCategoryView, category_view, category_list_view, like_view, AddCommentView

urlpatterns = [
    path('article/edit/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_caregory/', AddCategoryView.as_view(), name='add_category'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('category/<str:cats>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('atricle/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
