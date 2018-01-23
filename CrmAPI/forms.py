#-*- coding:utf-8 -*-
from django import forms
import re
from django.core.exceptions import ValidationError

# def user_validator(value):
#     user_reg = re.compile(r'^[0-9A-Za-z_]{8}')
#     if not user_reg.search(value):
#         raise ValidationError('用户名格式错误')
#
# class SignInForm(forms.Form):
#     username = forms.CharField(max_length=8,
#                                widget=forms.TextInput(attrs={'placeholder': '用户名'}),
#                                validators=[user_validator,])
#     password = forms.CharField(max_length=8)
#     mobile_value = forms.IntegerField()
#     sip_value = forms.IntegerField()
#
#     class Meta:
#         fields = ('username', 'password', 'mobile_value')
