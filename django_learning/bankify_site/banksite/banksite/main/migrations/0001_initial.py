# Generated by Django 4.1.2 on 2022-11-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=10)),
                ('uniqueid', models.IntegerField()),
                ('memo', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=2)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]