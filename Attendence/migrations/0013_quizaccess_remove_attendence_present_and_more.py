# Generated by Django 4.0.4 on 2022-05-22 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence', '0012_quizdetails_answer10_option1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizAccess',
            fields=[
                ('id', models.CharField(max_length=10000, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'quizAccess',
            },
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='present',
        ),
        migrations.AddField(
            model_name='attendence',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendence',
            name='students_names',
            field=models.CharField(default=django.utils.timezone.now, max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendence',
            name='students_userNames',
            field=models.CharField(default=django.utils.timezone.now, max_length=100000),
            preserve_default=False,
        ),
    ]
