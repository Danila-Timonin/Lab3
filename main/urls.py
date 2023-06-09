from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),

    path('students_courses', views.students_courses, name='students_courses'),
    path('ege_courses', views.ege_courses, name='ege_courses'),
    path('course_edit', views.course_edit, name='course_edit'),
    path('course_delete/<int:course_id>', views.course_delete, name='course_delete'),
    path('course_add', views.course_add, name='course_add'),
    path('course_subscription/<int:course_id>/', views.course_subscription, name='course_subscription'),
    path('my_courses', views.my_courses, name='my_courses'),
    path('course_details/<int:course_id>', views.course_details, name='course_details'),

    path('course/<int:course_id>/delete/', views.course_delete_from_my_list, name='course_delete_from_my_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)