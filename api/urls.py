from . import views
from django.urls import path

urlpatterns = [
    # path('teacher/list', views.teacher_list),
    # path('teacher/detail/<int:id>/', views.teacher_detail),
    # path('teacher/create', views.teacher_create),
    # path('teacher/update/<int:id>/', views.teacher_update),
    # path('teacher/delete/<int:id>/', views.teacher_delete),
    # # subject
    # path('subject/list', views.subject_list),
    # path('subject/detail/<int:id>/', views.subject_detail),
    # #
    # path('teacher/', views.TeacherView.as_view()),
    # path('teacher/<int:id>/', views.TeacherView.as_view()),
    # path('teacher/view/', views.TeacherClassView.as_view()),

    path('subjects/', views.subject_list, name='subject-list'),
    path('subjects/<int:pk>/', views.subject_detail, name='subject-detail'),
    path('teachers/', views.teacher_list, name='teacher-list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher-detail'),
]