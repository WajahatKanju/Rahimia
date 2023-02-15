from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Teacher


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    context_object_name = "teachers"
    login_url = 'account_login'

class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    context_object_name = "teacher"
    template_name = 'teachers/teacher_detail.html'
    login_url = 'account_login'