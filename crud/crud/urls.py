from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # function based view
    # path('student/', views.student_api),

    # class based view
    path('student/', views.StudentAPI.as_view())
]
