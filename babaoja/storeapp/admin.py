from django.contrib import admin
from .models import Category, Product, Profile, Feedback
from django.contrib.auth.models import Group, User
# Register your models here.



class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Feedback)



admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
