# Generated by Django 3.0.4 on 2021-10-15 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderdeliverrecord',
            name='name',
            field=models.ForeignKey(blank=True, help_text='交付人', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='交付人'),
        ),
        migrations.AddField(
            model_name='workorderdeliverrecord',
            name='work_order',
            field=models.ForeignKey(help_text='所属工单', on_delete=django.db.models.deletion.CASCADE, to='personal.WorkOrder', verbose_name='所属工单'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approver', to=settings.AUTH_USER_MODEL, verbose_name='初审人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='final_approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='final_approver', to=settings.AUTH_USER_MODEL, verbose_name='终审人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='proposer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposer', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='todoer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todoer', to=settings.AUTH_USER_MODEL, verbose_name='当前处理人'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='up_todoer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='up_todoer', to=settings.AUTH_USER_MODEL, verbose_name='上级处理人'),
        ),
        migrations.AddField(
            model_name='subworkorder',
            name='initiator',
            field=models.ForeignKey(blank=True, help_text='发起人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initiator', to=settings.AUTH_USER_MODEL, verbose_name='发起人'),
        ),
        migrations.AddField(
            model_name='subworkorder',
            name='work_order',
            field=models.ForeignKey(help_text='所属工单', on_delete=django.db.models.deletion.CASCADE, to='personal.WorkOrder', verbose_name='所属工单'),
        ),
        migrations.AddField(
            model_name='envcreatedetail',
            name='linkman',
            field=models.ForeignKey(blank=True, help_text='接口人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link_man', to=settings.AUTH_USER_MODEL, verbose_name='接口人'),
        ),
        migrations.AddField(
            model_name='dbrecoveryorder',
            name='safeman',
            field=models.ForeignKey(blank=True, help_text='脱敏审核人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='safeman', to=settings.AUTH_USER_MODEL, verbose_name='脱敏审核人'),
        ),
    ]