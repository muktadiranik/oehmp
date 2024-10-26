# Generated by Django 3.2.5 on 2023-04-13 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0005_auto_20230408_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredefinedAppointmentFollowUpCombination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predefined_appointment_follow_up_created_by', to=settings.AUTH_USER_MODEL)),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predefined_appointment_follow_up_diagnostic', to='common.diagnostic')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predefined_appointment_follow_up_treatment', to='common.treatment')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predefined_appointment_follow_up_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PredefinedAppointmentFollowUpCombinations',
            },
        ),
    ]
