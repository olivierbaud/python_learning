# Generated by Django 4.1.2 on 2022-11-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_operations_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='operations',
            name='uniqueid',
            field=models.IntegerField(unique=True),
        ),
    ]
