from django.urls import path
from .views import StudentListView, StudentDetailView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('<uuid:pk>', StudentDetailView.as_view(), name='student_detail'),
    
    # ? Ajax Calls
]
