from django.shortcuts import render
from django.views.generic import CreateView

from main.forms import Registration
 
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# def registration(request):
#     return render(request, 'main/registration.html')


class AddUser(CreateView):
    form_class = Registration
    template_name = 'main/registration.html'
    context_object_name = 'users'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     context['title'] = 'Добавление статьи'
    #     return context