from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required,'get')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm  # 어떤 폼을 입력받아서 할 것인지
    template_name = 'profileapp/create.html'


    def form_valid(self, form):  # form : 클라이언트가 데이터를 넣어놓은 ProfileCreationForm
        form.instance.user = self.request.user  # 유저 특정해주기, 폼이 생성되면
        return super().form_valid(form)

    def get_success_url(self):
       return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
