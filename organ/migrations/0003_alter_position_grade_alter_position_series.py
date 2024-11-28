# Generated by Django 5.1.3 on 2024-11-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0002_alter_position_grade_alter_position_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='grade',
            field=models.CharField(choices=[('01', '员级'), ('02', '初级'), ('03', '中级'), ('04', '高级'), ('05', '专家')], default='01', max_length=100, verbose_name='position grade'),
        ),
        migrations.AlterField(
            model_name='position',
            name='series',
            field=models.CharField(choices=[('A', '管理/行政类'), ('S', '营销/市场类'), ('T', '技术/研发类'), ('P', '生产/操作类')], default='A', max_length=1, verbose_name='position series'),
        ),
    ]
