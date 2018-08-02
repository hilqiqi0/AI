from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['uphone','upwd']
        labels={
            'uphone':'手机号',
            'upwd':'密码',
        }
        widgets={
            'uphone':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'upwd':forms.PasswordInput(
                attrs={
                    'placeholder':'请输入6-20位号码字符',
                    'class':'form-control',
                }
            )
        }