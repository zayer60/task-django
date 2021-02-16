from django.urls import path
from .views import ArticleDetailView, ArticleListView, CreateArticle, UpdateArticle, \
    DeleteArticle, ArticleYearArchive, ArticleMonthArchive, ArticleWeekArchive, ArticleDayArchive, \
    CSVGenerate, CSVToday
from django.views.generic.dates import ArchiveIndexView
from .models import Article

urlpatterns = [
    path('article/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/create/', CreateArticle.as_view(), name='create-article'),
    path('article/<int:pk>/edit/', UpdateArticle.as_view(), name='update-article'),
    path('article/delete/<int:pk>', DeleteArticle.as_view(), name='delete-article'),
    path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name='article_archive'),
    path('article/<int:year>/', ArticleYearArchive.as_view(), name="article-year"),
    path('article/<int:year>/<int:month>/', ArticleMonthArchive.as_view(month_format='%m'), name="article-month"),
    path('article/<int:year>/<str:month>/', ArticleMonthArchive.as_view(), name="article-month"),
    path('article/<int:year>/week/<int:week>', ArticleWeekArchive.as_view(), name="article-week"),
    path('article/<int:year>/<str:month>/<int:day>', ArticleDayArchive.as_view(), name="article-day"),
    path('article/csv/', CSVGenerate.as_view(), name="generate-csv"),
    path('article/csvtoday/', CSVToday.as_view(), name="generate_csv_today"),
]
