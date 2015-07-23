#coding:utf-8
from django.contrib import admin
from blog.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('status','create_time')
    list_display = ('name','parent','rank','status')
    fields = ('name','parent','rank','status')

class NewsAdmin(admin.ModelAdmin):
    search_fields = ('title','summary')
    list_filter = ('news_from','create_time')
    list_display = ('title','news_from','url','create_time')
    fields = ('title','news_from','url','summary','pub_time')

class NavAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','url','status','create_time')
    list_filter = ('status','create_time')
    fields = ('name','url','status')

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title','summary')
    list_filter = ('status','category','create_time','is_top')
    list_display = ('title','category','status','is_top','pub_time')
    fieldsets = (
        (u'基本信息', {
            'fields': ('title','en_title','img','category','is_top','rank','status')
            }),
        (u'内容', {
            'fields': ('content',) 
            }),
        (u'摘要', {
            'fields': ('summary',) 
            }),
        (u'时间', {
            'fields': ('pub_time',) 
            }),
    )

class CarouselAdmin(admin.ModelAdmin):
	search_fields = ('title',)
	list_filter =('create_time',)
	list_display = ('title','article','create_time',)
	fields = ('title','img','article','summary',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Nav,NavAdmin)
admin.site.register(Carousel,CarouselAdmin)