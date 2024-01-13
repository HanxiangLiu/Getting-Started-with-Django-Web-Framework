from django.urls import path

from .views import index, courses, course, add_a_b


urlpatterns = [
        path('', index),
        path('courses', courses),
        path('course/<int:id>', course),
        path('add/<int:a>/<int:b>', add_a_b)
]