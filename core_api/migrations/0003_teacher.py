# Generated by Django 4.1.3 on 2023-06-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0002_student_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
