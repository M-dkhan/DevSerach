from .models import Project
from django.forms import ModelForm, fields
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','featured_image' , 'source_link', 'demo_link', 'tags',]