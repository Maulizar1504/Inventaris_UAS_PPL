from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_barang_tampil_di_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='featured',
            field=models.BooleanField(default=False, help_text='Tandai sebagai featured untuk prioritas tampilan di landing page'),
        ),
    ]
