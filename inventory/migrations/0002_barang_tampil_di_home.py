from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='tampil_di_home',
            field=models.BooleanField(default=True, help_text='Tampilkan barang ini di halaman utama (landing page)'),
        ),
    ]
