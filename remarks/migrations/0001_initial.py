# Generated by Django 5.1.4 on 2025-01-08 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='given_remarks', to='authentication.counselor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remarks', to='authentication.student')),
            ],
        ),
    ]