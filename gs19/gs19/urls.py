from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# creating Router Object
router = DefaultRouter()

# register StudentViewSet with Router
router.register('studentapi', views.StudentReadonlyView, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
