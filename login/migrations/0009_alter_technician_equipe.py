# Generated by Django 4.2 on 2023-05-13 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_technician_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='equipe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to='login.equipe'),
        ),
    ]
