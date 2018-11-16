from django.contrib import admin
from .models import Categories,Technologies,Colors,Countries,Project,Profile

# Register your models here.
admin.site.register(Categories)
admin.site.register(Technologies)
admin.site.register(Colors)
admin.site.register(Countries)
admin.site.register(Project)
admin.site.register(Profile)
