from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('view-history/', views.view_history, name='view_history'),
]
