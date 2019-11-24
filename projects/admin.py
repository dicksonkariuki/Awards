from django.contrib import admin
from.models import categories
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('technologies','categories','colors')
# Register your models here.
admin.site.register(categories)
