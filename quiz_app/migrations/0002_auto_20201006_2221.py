# Generated by Django 3.1.2 on 2020-10-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.IntegerField(),
        ),
    ]