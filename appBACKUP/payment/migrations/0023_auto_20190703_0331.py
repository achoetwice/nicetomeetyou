# Generated by Django 2.2 on 2019-07-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0022_auto_20190703_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guesttemporaryinfo',
            name='id',
            field=models.CharField(default='c592636f', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]