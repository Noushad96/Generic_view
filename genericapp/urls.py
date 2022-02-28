from django.contrib import admin
from django.urls import path
from genericapp import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('student/',views.post_student, name="POST_student"),
    path('generic-student/',StudentGeneric.as_view())
    # path('generic-student/',StudentGeneric.as_view()),
]