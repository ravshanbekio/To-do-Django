# Generated by Django 3.2.9 on 2022-03-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220323_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]