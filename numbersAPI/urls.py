from django.urls import path
from . import views

urlpatterns = [
    path("classify-number/<int:num>/math",views.classify_number, name="get_number")
]