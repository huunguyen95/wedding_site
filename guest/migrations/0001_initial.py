# Generated by Django 4.0.2 on 2022-10-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('number_of_guest', models.CharField(max_length=200)),
                ('attending', models.TextField(blank=True, null=True)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]