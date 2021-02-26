from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('User', views.UserListAPIView.as_view(), name="User"),
    path('User/<int:id>', views.UserDetailAPIView.as_view(),
         name="User-partial-id"),

    path('Skill', views.SkillListAPIView.as_view(), name="Skill"),
    path('Skill/<int:id>', views.SkillDetailAPIView.as_view(),
         name="Skill-partial-id"),

    path('Project', views.ProjectListAPIView.as_view(), name="Project"),
    path('Project/<int:id>', views.ProjectDetailAPIView.as_view(),
         name="Project-partial-id"),

    path('Task', views.TaskListAPIView.as_view(), name="Task"),
    path('Task/<int:id>', views.TaskDetailAPIView.as_view(),
         name="Task-partial-id"),

    path('TaskSkillsRequired', views.TaskSkillsRequiredListAPIView.as_view(),
         name="TaskSkillsRequired"),
    path('TaskSkillsRequired/<int:id>', views.TaskSkillsRequiredDetailAPIView.as_view(),
         name="TaskSkillsRequired-partial-id"),

    path('Applicant', views.SkillListAPIView.as_view(), name="Applicant"),
    path('Applicant/<int:id>', views.ApplicantDetailAPIView.as_view(),
         name="Applicant-partial-id"),

    path('Contributor', views.ContributorListAPIView.as_view(), name="Contributor"),
    path('Contributor/<int:id>', views.ContributorDetailAPIView.as_view(),
         name="Contributor-partial-id"),

    path('UserRating', views.UserRatingListAPIView.as_view(), name="UserRating"),
    path('UserRating/<int:id>', views.UserRatingDetailAPIView.as_view(),
         name="UserRating-partial-id"),

    path('open_close_project/', views.open_close_project,
         name="open_close_project"),
    path('browse_jobs/', views.browse_jobs, name='browse_jobs'),
    path('jobs_update/', views.jobs_update, name='jobs_update'),
    path('form_state/', views.form_state, name='form_state'),
    path('post_project/', views.post_project, name='post_project'),
    path('project_description/<int:project_id>/',
         views.project_description, name='project_description'),
    path('<int:project_id>/add_task/', views.add_task, name='add_task'),
    path('<int:project_id>/task_description/<int:task_id>/',
         views.task_description, name='task_description'),
    path('<int:project_id>/task_edit/<int:task_id>/',
         views.task_editfunction, name='task_edit'),
    path('profile/<username>/', views.user_profile, name="profile"),
    path('myprojects/', views.myprojects, name="myprojects"),
    path('applicants/<int:task_id>/', views.applicants, name="applicants")
]
