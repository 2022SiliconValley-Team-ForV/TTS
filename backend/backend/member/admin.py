from django.contrib import admin

from .models import Member, ModelLink

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'birth', 'tmi', 'image_link')
    search_fields =  ('name',)

class ModelLinkAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Member, MemberAdmin)
admin.site.register(ModelLink, ModelLinkAdmin)