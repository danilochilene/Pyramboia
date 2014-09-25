from django.contrib import admin
from .models import Project, Target, Header, Argument, Task, History

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
        list_display = ('project_name','description')

class TargetAdmin(admin.ModelAdmin):
        list_display = ('url',)

class HeadersAdmin(admin.ModelAdmin):
        list_display = ('name','soapaction')

class ArgumentsAdmin(admin.ModelAdmin):
        list_display = ('name',)

class TasksAdmin(admin.ModelAdmin):
        list_display = ('project_name','task_name')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(Header, HeadersAdmin)
admin.site.register(Argument, ArgumentsAdmin)
admin.site.register(Task, TasksAdmin)
