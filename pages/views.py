from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Context

from students.models import Student


# Create your views here.
class HomePageView(TemplateView):
  # print(self.request)
  template_name = 'index.html'
  title = "home"

  def get_context_data(self, **kwargs: any) -> dict[str, any]:
    context = super().get_context_data(**kwargs) 
    students = Student.objects.all()
    context['students'] = students
    return context


class AboutPageView(TemplateView):
  # print(self.request)
  template_name = 'about.html'
  title = "about"

  def get_context_data(self, **kwargs: any) -> dict[str, any]:
    context = super().get_context_data(**kwargs)
    context['about_text'] = "Rahimia Institute of Quranic Sciences strives to foster collectivism and instil unity of thought among the responsible youth of the country. With its campuses located throughout the country, Rahimia Institute is rapidly preparing conscientious, intelligent, socially-aware human resource equipped to take on the challenge of development of our country.\n"
    context['about_text'] += "\tRahimia Institute considers the youth of this country an asset which must be valued, nurtured and groomed to accept the responsibility of our society. The (Rahimia) institute manages to do this by proactively engaging the youth through various seminars, discussion forums, Friday prayer congregations, and numerous other activities. Moreover, the primary objective of all these aforementioned activities is to instil, among Pakistani youth, the significance of systematically understanding the principles of a worthy society laid out in the light of the Quran."
    return context
