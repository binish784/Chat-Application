# Generated by Django 2.0 on 2019-04-13 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
