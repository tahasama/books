from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username',)

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'username',)

#how to add fields in SignupForm

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=False)
        self.fields['last_name'] = forms.CharField(required=False)

    def save(self, request):
        #first_name = self.cleaned_data.pop('first_name') #do not save first_name
        #last_name = self.cleaned_data.pop('last_name')
        user = super(MyCustomSignupForm, self).save(request)
        return user