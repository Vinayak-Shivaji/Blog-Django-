from django.forms import ModelForm
from .models import *

class Form(ModelForm):
     class meta:
          model=post
          fields=["title","body"]
     
     