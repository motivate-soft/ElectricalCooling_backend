from django.urls import path
from cooling import views

urlpatterns = [
    path('cooling',
         views.CoolingListView.as_view(),
         name='cooling-list'),
    path('cooling/<int:pk>',
         views.CoolingDetailView.as_view(),
         name='cooling-detail'),
    path('cooling/me',
         views.MyCoolingListView.as_view(),
         name='mycooling-list'),
    path('cooling/me/<int:pk>',
         views.CoolingDetailView.as_view(),
         name='cooling-detail'),
    path('cooling/demo_model',
         views.get_demo_model,
         name='cooling-detail'),
    path('cooling/solve',
         views.solve_thermal_model)
]
