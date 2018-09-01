#-*- coding: UTF-8 -*-
from django.contrib import admin
from stockapp.models import *

# Register your models here.
class StockAdmin(admin.ModelAdmin):
    #决定哪些是展开显示，哪些合并在一起
    fieldsets = (
        #这些展开
        (None, {
                'fields': ('number','company_name','user')
            }
        ),
        #这些默认合并
        ('高级设置',{
                'classes':('collapse',),
                'fields':('flow_in','flow_out',)
            }
        ),
    )
    #定义显示已保存文章的哪些字段
    list_display = ('number','company_name','impressum',)
    #定义是否显示链接
    list_display_links = ('number','company_name',)
    #设置哪些字段可以直接编辑
    list_editable = ('impressum',)
    #定义可以按照哪些字段分列
    list_filter = ('number','company_name',)

admin.site.register(User)
admin.site.register(Deal)
admin.site.register(Hold)
admin.site.register(Stock,StockAdmin)
admin.site.register(Link)
