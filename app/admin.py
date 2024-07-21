from django.contrib import admin

# Register your models here.

from .models import *

class what_you_learn_TabularInLine(admin.TabularInline):
    model = What_you_learn

class Requirements_TabularInLine(admin.TabularInline):
    model = Requirements

class Video_TabularInLine(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inLines =(what_you_learn_TabularInLine,Requirements_TabularInLine)



admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)

admin.site.register(Level)
admin.site.register(What_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Language)
admin.site.register(UserCource)
admin.site.register(Payment)


