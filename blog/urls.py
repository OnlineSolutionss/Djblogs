from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homepage'),
    path('post-by-tag/<str:by_tags>/', views.home, name='by_tags'),
    path('post-by-category/<str:by_category>/', views.home, name='by_category'),

    path("search/",views.post_searcher, name="search_post"),


    path('detail-page/<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

