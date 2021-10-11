from django.contrib import admin

from adoptions.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','breed','species','age','sex']

    # @display(description='Upper Case Name')
    # def upper_case_name(self,obj):
    #     return f'{obj.name.upper()}'

