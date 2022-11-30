from django.urls import path
from . import views


urlpatterns = [
    path('', views.submitData),
    path('<int:id>', views.pereval_detail_update),
]
