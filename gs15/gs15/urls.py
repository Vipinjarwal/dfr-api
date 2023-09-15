
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentc/', views.StudentCreate.as_view()),
    # path('studentr/<int:pk>', views.StudentRetrieve.as_view()),
    # path('studentu/<int:pk>', views.StudentUpdate.as_view()),
    # path('studentd/<int:pk>', views.StudentDestroy.as_view()),
    
    path('studentc/', views.StudentListCreate.as_view()),
    path('studentru/<int:pk>', views.StudentRetrieveUpdate.as_view()),
    path('studentrd/<int:pk>', views.StudentRetrieveDestroy.as_view()),
    path('studentrud/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),

]
