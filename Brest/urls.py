from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from work import views
from work.views import *

app_name = 'works'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('<int:pk>/', views.resize, name = 'resize'),
    path('api/v1/work/create', ImageCreateView.as_view()),
    path('api/v1/work/list', ImageListView.as_view()),
    path('api/v1/work/detail/<int:pk>/', ImageDetailView.as_view()),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
