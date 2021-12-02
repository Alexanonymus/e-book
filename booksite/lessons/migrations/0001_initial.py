# Generated by Django 3.2.9 on 2021-12-02 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thema', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('author', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.category')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('variant1', models.CharField(max_length=400)),
                ('variant2', models.CharField(max_length=400)),
                ('variant3', models.CharField(max_length=400)),
                ('variant4', models.CharField(max_length=400)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_questions', models.IntegerField(max_length=3)),
                ('true_ans', models.IntegerField(max_length=3)),
                ('false_ans', models.IntegerField(max_length=3)),
                ('test_date', models.IntegerField(max_length=3)),
                ('test', models.ManyToManyField(to='lessons.Tests')),
                ('username', models.ManyToManyField(to='lessons.Users')),
            ],
        ),
    ]