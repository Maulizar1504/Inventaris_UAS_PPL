from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_barang_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('nim', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telepon', models.CharField(blank=True, max_length=20, null=True)),
                ('alasan', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.barang')),
            ],
        ),
    ]
