from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('autoplot/', views.AutoPlot, name='AutoPlot'),
]