from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from auth_.models import User


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'surname',
            'patronymic',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''