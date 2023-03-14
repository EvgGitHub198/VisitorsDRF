from django.urls import path
from .views import *


urlpatterns = [
    path('visitors/', VisitorView.as_view()),
    path('visitors/<int:pk>/', VisitorView.as_view()),

]