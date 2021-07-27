from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile # 어떤 모델을 기반으로 할 것인지
        fields = ['image', 'nickname', 'message'] # 클라이언트에게 받을 것