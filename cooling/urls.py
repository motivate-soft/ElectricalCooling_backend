from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cooling import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('cooling/',
         views.CoolingListView.as_view(),
         name='cooling-list'),
    path('cooling/<int:pk>/',
         views.CoolingDetailView.as_view(),
         name='cooling-detail'),
])
