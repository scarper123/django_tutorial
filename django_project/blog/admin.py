from django.contrib import admin
from blog import models
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    '''
        Admin View for Author
    '''
    list_display = ('name', 'email', 'created_on')
    list_filter = ('active',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name', 'email')
    date_hierarchy = 'created_on'


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''
    list_display = ('name', 'slug')
    # list_filter = ('',)
    # inlines = [
    # Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title', 'slug', 'pub_date')
    list_filter = ('pub_date',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('title', 'slug',)


class TagAdmin(admin.ModelAdmin):
    '''
        Admin View for Tag
    '''
    list_display = ('name', 'slug')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name', 'slug',)


class FeedbackAdmin(admin.ModelAdmin):
    '''
        Admin View for Feedback
    '''
    # fields = ('name', 'email', 'subject')
    list_display = ('name', 'email', 'subject')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name', 'email', 'subject')


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Feedback, FeedbackAdmin)
