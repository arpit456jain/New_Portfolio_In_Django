# Generated by Django 3.1.3 on 2021-02-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
    ]
