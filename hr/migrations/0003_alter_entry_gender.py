# Generated by Django 5.1.3 on 2024-11-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_alter_employeesalaryitem_calculate_way_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='gender',
            field=models.CharField(choices=[('0', 'Unknown gender'), ('1', 'male'), ('2', 'female'), ('9', 'Unspecified gender')], default='1', max_length=100, verbose_name='gender'),
        ),
    ]
