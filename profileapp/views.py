from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm # 어떤 폼을 입력받아서 할 것인지
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):  # form : 클라이언트가 데이터를 넣어놓은 ProfileCreationForm
        form.instance.user = self.request.user  # 유저 특정해주기, 폼이 생성되면
        return super().form_valid(form)