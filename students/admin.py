from django.contrib import admin
from .models import Student, Evaluation_A, Evaluation_B, Evaluation_C


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name','CNIC', 'phone', 'permanent_address', 'current_address')

  def get_form(self, request,obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if request.user.is_superuser == False:
      form.base_fields['first_name'].disabled = True    
    return form


admin.site.register(Evaluation_A)
admin.site.register(Evaluation_B)
admin.site.register(Evaluation_C)