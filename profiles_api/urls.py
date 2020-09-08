from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from profiles_api import views
# https://www.django-rest-framework.org/api-guide/routers/


# register our url sub domain and this links to the class "HelloViewset" which will
# handle the client request 


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
