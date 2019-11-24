from django.contrib import admin
from.models import categories,technologies,colors,countries,Project,Profile,Rating
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('technologies','categories','colors')
# Register your models here.
admin.site.register(categories)
admin.site.register(technologies)