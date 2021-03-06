# Generated by Django 2.1.7 on 2019-05-18 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20190516_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('-done', '-due')},
        ),
        migrations.AddField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DUE'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='DESCRIPTION'),
        ),
    ]
