# Generated by Django 4.2 on 2023-04-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('R', 'Reviewed'), ('N', 'Not reviewed'), ('E', 'Error'), ('A', 'Accepted')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]
