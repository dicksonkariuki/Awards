from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username','post_date','design','usability','creativity','content','overall_score','avatar']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
