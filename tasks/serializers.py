from rest_framework import serializers
from authentication.models import User
from .models import Skill, UsersSkill, Project, Task, Applicant, UserRating, Contributor, TaskSkillsRequired


class UserTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'user', 'phone', 'about_me', 'profile_image']


class SkillTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'skill_name']


class UsersSkillTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersSkill
        fields = ['id', 'user', 'skill', 'level_of_proficiency']


class ProjectTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'description', 'postedOn',
                  'leader', 'isCompleted', 'deadline', 'task_count']


class TaskTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'addedOn', 'deadline', 'isCompleted', 'latest_submission_time',
                  'credits', 'rating', 'project', 'mention', 'amount', 'task_description', 'task_link']


class TaskSkillsRequiredTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSkillsRequired
        fields = ['id', 'task', 'skill', 'proficiency_level_required']


class ApplicantTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'task', 'user', 'time_of_application']


class ContributorTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'task',
                  'isCreditVerified', 'time_of_selection']


class UserRatingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = ['id', 'task', 'emp', 'fre', 'f_rating', 'e_rating']
