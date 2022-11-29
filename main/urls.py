from django.urls import path, include
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('perevals', views.PerevalCreate)


urlpatterns = [
    path('', views.submitData),
    # path('', views.submitData.as_view()),
    # path('', views.PerevalCreate.as_view()),
    # path('', include(router.urls))
]
