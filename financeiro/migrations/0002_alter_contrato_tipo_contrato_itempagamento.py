# Generated by Django 4.1.3 on 2022-11-23 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imoveis', '0006_imovel_descricao'),
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='tipo_contrato',
            field=models.CharField(choices=[('Compra', 'Compra'), ('Venda', 'Venda'), ('Alguel', 'Alguel')], max_length=100, null=True, verbose_name='Categoria'),
        ),
        migrations.CreateModel(
            name='ItemPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('valor_parcela', models.FloatField(blank=True, null=True, verbose_name='Valor da Parcela ')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('status', models.CharField(blank=True, choices=[('aprovado', 'aprovado'), ('pendente', 'pendente'), ('vencido', 'vencido')], default='pendente', max_length=500, null=True, verbose_name='Status do pagamento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='imoveis.imovel')),
            ],
            options={
                'verbose_name': 'Item pagamento',
                'verbose_name_plural': 'itens pagamento',
            },
        ),
    ]
