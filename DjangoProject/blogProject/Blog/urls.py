from django.urls import path

from .views import(
    ArticleListView,
    ArticleDetailView,
)

# as_view() turns it into a function based view
app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name="article-list"),
    path('<int:id>', ArticleDetailView.as_view(), name="article-detail"),
]