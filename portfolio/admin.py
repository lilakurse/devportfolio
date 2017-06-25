from django.contrib import admin

from .models import Profile, Resume
# Register your models here.

class PofileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location','birth_date')

admin.site.register(Profile, PofileAdmin)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('education', 'experience', 'user')

admin.site.register(Resume, ResumeAdmin)
