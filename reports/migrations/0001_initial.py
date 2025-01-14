# Generated by Django 5.1.4 on 2025-01-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_on', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=5)),
                ('report_file', models.FileField(upload_to='reports/')),
            ],
        ),
    ]
