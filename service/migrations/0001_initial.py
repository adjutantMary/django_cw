# Generated by Django 4.0 on 2024-08-15 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('comment', models.TextField(blank=True, max_length=320, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=128, null=True)),
                ('body', models.TextField(blank=True, max_length=320, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('period', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2)),
                ('status', models.CharField(blank=True, choices=[('D', 'Done'), ('C', 'Created'), ('L', 'Launched'), ('I', 'Inactive')], default='I', max_length=2, null=True)),
                ('clients', models.ManyToManyField(to='service.Client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.message')),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_success', models.BooleanField(default=False)),
                ('details', models.TextField(blank=True, null=True)),
                ('mailing_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.mailingsettings')),
            ],
        ),
    ]