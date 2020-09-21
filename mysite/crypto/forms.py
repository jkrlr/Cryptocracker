from django import forms
from django.contrib.auth.models import User
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# # class SinupForm(UserCreationForm):
# #     roll_no = forms.IntegerField()
# #     full_name = forms.CharField()
# #     email = forms.EmailField()
# #     phone_no = forms.IntegerField()

# #     class Meta:
# #         model = User
# #         fields = ['username', 'roll_no', 'full_name', 'email', 'phone_no', 'password1','password2']

# # class UserForm(forms.ModelForm):
# #     class Meta:
# #         model = User
# #         fields = ('first_name', 'last_name', 'email') 
 
class SinupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['roll','phone']




