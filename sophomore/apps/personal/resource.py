from import_export import resources
from .models import *


class WorkOrderResource(resources.ModelResource):
    class Meta:
        model = WorkOrder
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['number', 'title', 'content', 'type', 'status', 'is_show', 'is_return']


class EnvCreateDetailResource(resources.ModelResource):
    class Meta:
        model = EnvCreateDetail
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['id']


class DbRecoveryOrderResource(resources.ModelResource):
    class Meta:
        model = DbRecoveryOrder
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['id']


class FaultResolveOrderResource(resources.ModelResource):
    class Meta:
        model = FaultResolveOrder
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['id']


class SubWorkOrderResource(resources.ModelResource):
    class Meta:
        model = SubWorkOrder
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['id']


class WorkOrderDeliverRecordResource(resources.ModelResource):
    class Meta:
        model = WorkOrderDeliverRecord
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ['id']
