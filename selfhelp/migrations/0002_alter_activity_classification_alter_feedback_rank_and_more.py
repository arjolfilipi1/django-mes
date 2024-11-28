# Generated by Django 5.1.3 on 2024-11-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfhelp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='classification',
            field=models.CharField(blank=True, choices=[('T', 'Train'), ('M', 'Meeting'), ('G', 'Community')], default='M', max_length=100, null=True, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rank',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='B', max_length=100, null=True, verbose_name='rank'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'NEW'), ('I', 'IN PROGRESS'), ('A', 'APPROVED'), ('P', 'PAYED')], default='N', max_length=100, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'NEW'), ('I', 'IN PROGRESS'), ('A', 'APPROVED'), ('P', 'PAYED')], default='N', max_length=100, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='business_domain',
            field=models.CharField(choices=[('HR', '人事'), ('FI', '财务'), ('AD', '行政'), ('MA', '市场'), ('BU', '商务'), ('CS', '客服'), ('OT', '其他'), ('PO', '采购')], default='OT', max_length=4, verbose_name='business domain'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='classification',
            field=models.CharField(choices=[('S', '内部服务'), ('R', '设备维修'), ('Q', '问题咨询'), ('D', '采购申请')], default='D', max_length=4, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.CharField(blank=True, choices=[('NEW', '新建'), ('SCHE', '调度'), ('PROC', '处理'), ('CLOSE', '关闭')], default='NEW', max_length=6, null=True, verbose_name='status'),
        ),
    ]
