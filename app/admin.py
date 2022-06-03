from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__' #['title', 'photo', 'category', 'tags', 'content','slug']

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id','title', 'author', 'created_at', 'get_photo', 'views', 'category')
    list_display_links = ('id', 'title')
    save_on_top = True
    save_as = True
    search_fields = ('title','category')
    list_filter = ('title', 'category','tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo','views','created_at','author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=80>')
        return '-'
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    save_on_top = True
    save_as = True
    search_fields = ('title',)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    save_on_top = True
    save_as = True
    search_fields = ('title',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
