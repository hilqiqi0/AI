# -*- coding:utf-8 -*-
from django import forms

SEX_CHOICES = (
  ('0','男'),
  ('1','女'),
)

class LoginForm(forms.Form):
    '''
    登录Form，只需要用户名和密码
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})

class RegForm(forms.Form):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",}),
                              max_length=50,error_messages={"required": "username不能为空",})
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",}),
                              max_length=20,error_messages={"required": "password不能为空",})

    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",}),
                              max_length=50,error_messages={"required": "email不能为空",})

    gender = forms.ChoiceField(choices = SEX_CHOICES)

    age = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Age", "required": "required",}),
                            error_messages={"required": "请输入年龄",})
    profession = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "profession", "required": "required",}),
                              max_length=128,error_messages={"required": "profession不能为空",})
    #可以为空
    qq = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "qq", "required": "required",}),
                              max_length=11,error_messages={"required": "email不能为空",})
    #不能重复
    mobile = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "tel", "required": "required",}),
                              max_length=11,error_messages={"required": "mobile不能为空",})



