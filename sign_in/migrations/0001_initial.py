# Generated by Django 4.0.3 on 2022-06-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
            ],
        ),
    ]
