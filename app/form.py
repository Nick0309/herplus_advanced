from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=20, label="姓名")
    phone = forms.CharField(max_length=15, label="電話")
    email = forms.EmailField(label="電子信箱")