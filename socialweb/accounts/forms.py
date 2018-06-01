from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

 class UserCreateForm(UserCreationForm):
     
     class Meta:
         fields = ('username','email','password1','password2')  #comes in the get_user_model
         model = get_user_model()


     def __init__(self,*args,**kwargs):
         super().__init__(*args,**kwargs)
         self.fields['username'].label = 'Display Name' #label 
         self.fields['email'].label = 'Email Address'      
