from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Exemplo de validação simples de formato de email:
        if '@' not in username:
            raise forms.ValidationError(
                'Este campo deve ser um email válido.')
        return username


class CriarContaForm(UserCreationForm):
    # se o campo não for obrigatório dentro dos parenteses incluir (required=False)
    email = forms.EmailField()

    class Meta:  # Quando se cria um UserCreationForm ele espera uma class Meta indicando qual o modelo ele ira se basear
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Já existe uma conta com este e-mail.'
            )
        return email
