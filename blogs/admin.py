from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.


class RecepiInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecepiInLine]
    save_as = True 
    save_on_top = True

@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'perp_time', 'cook_time', 'post']
    
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag,)
admin.site.register(models.Post, PostAdmin)

