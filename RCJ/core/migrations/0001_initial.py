# Generated by Django 3.0.1 on 2020-02-05 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=11, unique=True, verbose_name='atalho')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=11, unique=True, verbose_name='RG')),
                ('date_of_birth', models.DateField(verbose_name='Data de Nascimento')),
                ('sex', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], max_length=1, verbose_name='Sexo')),
            ],
        ),
        migrations.CreateModel(
            name='ContatoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone_1', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone 1')),
                ('telefone_2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone 2')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='Rua')),
                ('number', models.IntegerField(verbose_name='Numero')),
                ('complement', models.CharField(max_length=50, verbose_name='Complemento')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro')),
                ('reference_point', models.CharField(blank=True, max_length=50, verbose_name='Ponto de referência')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='InfoAuditoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Auditor')),
                ('status_auditoria', models.CharField(choices=[('APROVADA', 'APROVADA'), ('REPROVADA', 'REPROVADA'), ('CONSULTAR', 'CONSULTAR'), ('CANCELADO', 'CANCELADO'), ('DESISTENCIA', 'DESISTENCIA'), ('CHECKLIST', 'CHECKLIST'), ('PENDENTE', 'PENDENTE')], default='PENDENTE', max_length=12, null=True, verbose_name='Status da Auditoria')),
                ('status_pos_venda', models.CharField(choices=[('HABILITADO', 'HABILITADO'), ('DESISTENCIA', 'DESISTÊNCIA'), ('EM ROTA', 'EM ROTA'), ('AGUARDANDO PAGAMENTO', 'AGUARDANDO PAGAMENTO')], default='AGUARDANDO PAGAMENTO', max_length=21, null=True, verbose_name='Status Pós venda')),
                ('observacoes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SKY', 'SKY'), ('OI', 'OI'), ('CLARO', 'CLARO'), ('TIM', 'TIM')], max_length=5, verbose_name='Nome')),
                ('plano', models.CharField(max_length=50, verbose_name='Plano')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='InfoVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal_da_venda', models.CharField(choices=[('ATIVO', 'ATIVO'), ('PREDITIVO', 'PREDITIVO'), ('DISCADOR', 'DISCADOR'), ('LEAD', 'LEAD'), ('REDES SOCIAIS', 'REDES SOCIAIS')], max_length=14, verbose_name='Canal da venda')),
                ('status_venda', models.CharField(choices=[('PRE APROVADA', 'PRE APROVADA'), ('REPROVADA', 'REPROVADA')], max_length=14, verbose_name='Status da Venda')),
                ('operador', models.CharField(max_length=50, verbose_name='Operador')),
                ('supervisor', models.CharField(max_length=50, verbose_name='Supervisor')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Data da venda')),
                ('adesao', models.CharField(choices=[('GRATIS', 'GRÁTIS'), ('INTEGRAL', 'INTEGRAL'), ('PARCIAL', 'PARCIAL')], max_length=10, verbose_name='Adesão')),
                ('forma_de_pagamento', models.CharField(choices=[('CARTAO DE CREDITO', 'CARTÃO DE CRÉDITO'), ('DEBITO EM CONTA', 'DÉBITO EM CONTA'), ('BOLETO BANCÁRIO', 'BOLETO BANCÁRIO')], max_length=17, verbose_name='Forma de pagamento')),
                ('observacoes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observações')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client', verbose_name='Cliente')),
                ('info_auditoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.InfoAuditoria', verbose_name='Informação Auditoria')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto', verbose_name='Produto')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='contato',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.ContatoCliente', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='client',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.EnderecoCliente', verbose_name='Endereço'),
        ),
    ]
