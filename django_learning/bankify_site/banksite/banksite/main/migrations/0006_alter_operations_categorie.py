# Generated by Django 4.1.2 on 2022-12-09 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_operations_categorie_alter_categories_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories'),
        ),
    ]