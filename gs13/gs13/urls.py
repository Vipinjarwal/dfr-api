
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('studentapi/<int:pk>', views.StudentRetrive.as_view()),
    path('stucre/', views.StudentCreate.as_view()),
    path('stuup/<int:pk>', views.StudentUpdate.as_view()),
    path('studel/<int:pk>', views.StudentDestroy.as_view()),
]
