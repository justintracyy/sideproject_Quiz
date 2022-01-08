# Generated by Django 3.2.5 on 2022-01-08 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECECoreSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=256)),
                ('number_of_questions', models.IntegerField()),
                ('require_score_to_pass', models.IntegerField()),
            ],
        ),
    ]
