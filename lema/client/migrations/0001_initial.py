# Generated by Django 5.0.6 on 2024-07-09 16:25

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('notes', models.TextField(blank=True, default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Ten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Nine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfTen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfNine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfEleven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='HalfEight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Four',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Five',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Eleven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Eight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.userinfo')),
            ],
        ),
    ]
