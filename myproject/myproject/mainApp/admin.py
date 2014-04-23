from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from datetime import datetime, timedelta

# Register your models here.

from myproject.mainApp.models import Plan, User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords do not match!")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.lastmodelcreation = (datetime.now() - timedelta(minutes=31)).replace(tzinfo=None)
            user.lastmodelevaluation = (datetime.now() - timedelta(minutes=6)).replace(tzinfo=None)
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_active', 'is_admin')


    def clean_password(self):
        return self.initial["password"]


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Actions', {'fields': ('lastmodelcreation', 'lastmodelevaluation')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}),
    )

    search_fields = ('email', 'username')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(Plan)
admin.site.register(User, UserAdmin)

#we are not using django's built-in permissions,
admin.site.unregister(Group)