from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-info/<int:pk>', views.student_detail),
    path('student-list/', views.student_list),
]
