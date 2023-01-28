from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContractForm
from classroom.models import Teacher

# Create your views here.

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class ContactFormView(FormView):
    form_class = ContractForm
    template_name = "classroom/contact.html"

    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherListView(ListView):
    model = Teacher
    #Default
    queryset = Teacher.objects.all()
    context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:teacher_list")

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')