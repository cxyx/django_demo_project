from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import *
from django.http import JsonResponse

admin.site.site_header = 'sophomore管理后台'  # 设置header
admin.site.site_title = 'sophomore管理后台1'  # 设置title
admin.site.index_title = 'sophomore管理后台2'

from simpleui.admin import AjaxAdmin


@admin.register(WorkOrder)
class WorkOrderAdmin(ImportExportModelAdmin):
    resource_class = WorkOrderResource
    list_display = [
        'number',
        'title',
    ]
    search_fields = [
        'number',
        'title',
    ]
    list_filter = [
        'number',
        'title',
    ]
    list_per_page = 100


@admin.register(EnvCreateDetail)
class EnvCreateDetailAdmin(ImportExportModelAdmin):
    resource_class = EnvCreateDetailResource
    list_display = [
        'id',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    list_per_page = 100


@admin.register(DbRecoveryOrder)
class DbRecoveryOrderAdmin(ImportExportModelAdmin):
    resource_class = DbRecoveryOrderResource
    list_display = [
        'id',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    list_per_page = 100


@admin.register(FaultResolveOrder)
class FaultResolveOrderAdmin(ImportExportModelAdmin):
    resource_class = FaultResolveOrderResource
    list_display = [
        'id',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    list_per_page = 100


@admin.register(SubWorkOrder)
class SubWorkOrderAdmin(ImportExportModelAdmin):
    resource_class = SubWorkOrderResource
    list_display = [
        'id',
        'number',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    list_per_page = 100


@admin.register(WorkOrderDeliverRecord)
class WorkOrderDeliverRecordAdmin(ImportExportModelAdmin):
    resource_class = WorkOrderDeliverRecord
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
    ]
    list_filter = [
        'id',
    ]
    list_per_page = 100

