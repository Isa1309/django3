# Generated by Django 4.0.2 on 2022-02-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_birth', models.DateField()),
                ('interesting_facts', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]