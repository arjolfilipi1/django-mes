# Generated by Django 5.1.3 on 2024-11-27 09:35

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basedata', '0002_brand_measure_address_category_dataimport_document_and_more'),
        ('organ', '0002_alter_position_grade_alter_position_series'),
        ('selfhelp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('order_date', models.DateField(verbose_name='order date')),
                ('arrive_date', models.DateField(verbose_name='arrive date')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('4', 'DROP'), ('9', 'APPROVED'), ('99', 'ALREADY STOCK IN')], default='0', max_length=2, verbose_name='status')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='money amount')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='discount amount')),
                ('entry_status', models.BooleanField(default=0, verbose_name='entry status')),
                ('entry_time', models.DateTimeField(blank=True, null=True, verbose_name='entry time')),
                ('attach', models.FileField(blank=True, help_text='您可导入采购明细，模板请参考文档FD0008', null=True, upload_to='', verbose_name='attach')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.organization', verbose_name='organization')),
                ('partner', models.ForeignKey(limit_choices_to={'partner_type': 'S'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.partner', verbose_name='partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'purchase order',
                'verbose_name_plural': 'purchase orders',
            },
        ),
        migrations.CreateModel(
            name='POItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='price')),
                ('cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='count')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='discount price')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='money of amount')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='discount amount')),
                ('tax', models.CharField(choices=[], default='0.00', max_length=6, verbose_name='tax rate')),
                ('is_in_stock', models.BooleanField(default=0, verbose_name='is in stock')),
                ('in_stock_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('entry_cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='entry count')),
                ('left_cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='left count')),
                ('material', models.ForeignKey(limit_choices_to={'is_virtual': '0'}, on_delete=django.db.models.deletion.CASCADE, to='basedata.material', verbose_name='material')),
                ('measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basedata.measure', verbose_name='measure')),
                ('woitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='selfhelp.woitem', verbose_name='wo item')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchaseorder', verbose_name='purchase order')),
            ],
            options={
                'verbose_name': 'po item',
                'verbose_name_plural': 'po item',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('py_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='pay date')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='pay code')),
                ('po_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='po amount')),
                ('py_amount', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='pay amount')),
                ('response_code', models.CharField(blank=True, max_length=80, null=True, verbose_name='response code')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='memo')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basedata.bankaccount', verbose_name='bank account')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.organization', verbose_name='organization')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basedata.partner', verbose_name='partner')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchaseorder', verbose_name='purchase order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('vo_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='invoice date')),
                ('code', models.CharField(max_length=20, verbose_name='invoice code')),
                ('number', models.CharField(max_length=20, verbose_name='invoice number')),
                ('po_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='po amount')),
                ('vo_amount', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='invoice amount')),
                ('file', models.FileField(blank=True, null=True, upload_to='invoice', verbose_name='invoice file')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basedata.partner', verbose_name='partner')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchaseorder', verbose_name='purchase order')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoice',
            },
        ),
    ]
