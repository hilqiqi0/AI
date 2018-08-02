from django.contrib import admin
from .models import *

#声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    # 1.指定在列表页中显示的字段们
    list_display=['names','age','email']
    # 2.指定能够链接到详情页的字段们
    list_display_links=['names','email']
    # 3.指定在列表页中就允许被编辑的字段们
    list_editable = ['age']
    # 4.添加允许被搜索的字段们
    search_fields = ['names','email']
    # 5.增加右侧过滤器，实现快速筛选
    list_filter=['names','email']
    # 6.指定在详情页中显示的字段们以及排列的顺序
    # fields = ['email','names','age']
    # 7.指定字段的分组
    # fieldsets = (
    #     #分组１
    #     (
    #         '基本信息',{
    #             'fields':('names','email'),
    #         }
    #     ),
    #     #分组２
    #     (
    #         '可选信息',{
    #             'fields':('age','isActive'),
    #             'classes':('collapse',),
    #         }
    #     )
    # )

# 编写Book的高级管理类
class BookAdmin(admin.ModelAdmin):
    # 1.增加时间选择器
    date_hierarchy='publicate_date'

# 编写Publisher的高级管理类
class PublisherAdmin(admin.ModelAdmin):
    # 1.列表页显示name,address,city,website
    list_display = ['name','address','city','website']
    # 2.address 和　city 是可编辑的
    list_editable = ['address','city']
    # 3.右侧增加过滤器，允许按照address和city筛选
    list_filter = ['address','city']
    # 4．分组显示,name,address,city 为基本选项,country和website为可选选项，并可折叠
    fieldsets = (
        (
            '基本选项',{
                'fields':('name','address','city'),
            }
        ),
        (
            '可选选项',{
                'fields':('country','website'),
                'classes':('collapse',),
            }
        )
    )


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)
