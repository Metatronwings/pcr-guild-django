# Generated by Django 3.0.6 on 2020-05-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200521_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='48abe5cc9b1611ea8a3ed46d6df5224b', max_length=36, primary_key=True, serialize=False),
        ),
    ]
