# Generated by Django 2.2.9 on 2020-02-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('password', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
