# Generated by Django 2.0.7 on 2018-09-08 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20180908_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.City'),
        ),
    ]
