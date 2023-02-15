from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, FormView

from .models import Student
from administrative_divisions.models import Halqa, Zone, Region, Province


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = "students"
    login_url = 'account_login'    
    
    
    def load_regions(self):
        province_id = self.request.GET.get('id_province')
        regions = Region.objects.filter(province_id=province_id)
        # cities = City.objects.filter(country_id=country_id).order_by('name')
        # return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})
        
    def get_queryset(self):
        return Student.objects.all()
    
class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = "student"
    template_name = 'students/student_detail.html'
    login_url = 'account_login'

