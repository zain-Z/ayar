from django.db import models
from authentication.models import User
import os


class Skill(models.Model):
    skill_name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.skill_name


class UsersSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level_of_proficiency = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.user.username) + "/" + str(self.skill.skill_name) + "/" + str(self.level_of_proficiency)


class Project(models.Model):
    project_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, default=None)
    postedOn = models.DateTimeField(auto_now_add=True, blank=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)
    task_count = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False)
    addedOn = models.DateTimeField(auto_now_add=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    credits = models.CharField(max_length=20, choices=(("Paid", "Paid"), ("Other", "Other")), blank=False,
                               default="Paid")
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    mention = models.CharField(max_length=200, blank=True, null=True)
    amount = models.IntegerField(default=0)
    task_description = models.CharField(max_length=100, default=None)
    task_link = models.URLField(blank=True)
    latest_submission_time = models.DateTimeField(blank=True, null=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)

    def __str__(self):
        return self.task_name


class TaskSkillsRequired(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level_required = models.IntegerField(1)

    def __str__(self):
        return str(self.task.task_name) + '[id=' + str(self.task.id) + ']'


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time_of_application = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user.user.username) + '[id=' + str(self.user.id) + ']'


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    isCreditVerified = models.BooleanField(default=False)
    time_of_selection = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user.user.username) + '[id=' + str(self.user.id) + ']'


class UserRating(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    emp = models.ForeignKey(
        User, related_name='rating_by', on_delete=models.CASCADE)
    fre = models.ForeignKey(
        User, related_name='rating_to', on_delete=models.CASCADE)
    f_rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    e_rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    def __str__(self):
        return str(self.task.id)+"--"+str(self.fre.user.username)+"--"+str(self.emp.user.username)
