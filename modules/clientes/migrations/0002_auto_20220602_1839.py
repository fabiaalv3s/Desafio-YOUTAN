from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='cnpj',
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('filial_name', models.CharField(max_length=50, verbose_name='Empresa')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clients', verbose_name='Empresa')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
