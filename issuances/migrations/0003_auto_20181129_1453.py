# Generated by Django 2.1.3 on 2018-11-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuances', '0002_auto_20181129_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chaptersection',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='chaptersection',
            name='position',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Position'),
        ),
    ]
