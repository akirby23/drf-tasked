# Generated by Django 3.2.25 on 2024-03-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20240319_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_on']},
        ),
    ]