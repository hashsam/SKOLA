# Generated by Django 5.0.6 on 2024-07-13 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_course_certificate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usercource')),
            ],
        ),
    ]
