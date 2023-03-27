# from django import forms
# from django.contrib.auth.forms import UserCreationForm


# class registerform(UserCreationForm):
    
#     first_name=forms.CharField(max_length=50)
#     last_name=forms.CharField(max_length=50)
#     date_of_birth=forms.CharField(max_length=50)
#     address=forms.CharField(max_length=50)


#     class meta:
#         model=User
#         fields=('username','password1','password2','first_name','last_name','address')

#     def save(self,commit=True):
#         user=super(registerform,self).save(commit=false)
#         user.first_name=self.cleaned_data['first_name']
#         user.last_name=self.cleaned_data['last_name']
#         user.address=self.cleaned_data['address']


#         if commit:
#             user.save()
#         return user
