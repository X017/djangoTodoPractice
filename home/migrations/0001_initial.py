# Generated by Django 5.1.2 on 2024-10-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Body', models.CharField(max_length=256)),
                ('finish', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]