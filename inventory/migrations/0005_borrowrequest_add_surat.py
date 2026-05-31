from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_borrowrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrequest',
            name='surat',
            field=models.FileField(blank=True, null=True, upload_to='surat/', help_text='Unggah surat permohonan/pengantar (PDF/JPG/PNG)'),
        ),
    ]
