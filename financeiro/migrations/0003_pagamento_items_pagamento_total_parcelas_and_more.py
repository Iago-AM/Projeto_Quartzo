# Generated by Django 4.1.3 on 2022-11-23 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financeiro', '0002_alter_contrato_tipo_contrato_itempagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='items',
            field=models.ManyToManyField(to='financeiro.itempagamento'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='total_parcelas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Parcelas'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Funcionario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='pagamento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.pagamento'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='tipo_contrato',
            field=models.CharField(choices=[('Compra', 'Compra'), ('Venda', 'Venda'), ('Aluga', 'Aluga')], max_length=100, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='itempagamento',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_cliente', to=settings.AUTH_USER_MODEL),
        ),
    ]
