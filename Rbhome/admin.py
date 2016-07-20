from django.contrib import admin
from django.contrib.auth.models import User
from models import Userprofile,BackyardModel
# Register your models here.

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = Userprofile

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    fields = ('username', 'email')

admin.site.register(User, UserAdmin)
admin.site.register(BackyardModel)
