# Generated by Django 3.2.6 on 2022-04-14 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence', '0003_studentdetails_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='classaccess',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]