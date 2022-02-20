from django.contrib import admin
from django.urls import path

from content.views import PageListApiView, PageDetailApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageListApiView.as_view()),
    path('<int:pk>/', PageDetailApiView.as_view(), name='page_detail')
]
