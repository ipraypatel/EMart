# Generated by Django 3.1.2 on 2020-10-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=10)),
                ('emailid', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
