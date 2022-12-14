# Generated by Django 4.1.4 on 2022-12-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('employee_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact_Number', models.IntegerField()),
                ('emergency_Contact_Number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('dOB', models.DateField()),
                ('martial_Status', models.CharField(max_length=100)),
                ('blood_Group', models.CharField(max_length=100)),
                ('job_Title', models.CharField(max_length=100)),
                ('work_Location', models.CharField(max_length=100)),
                ('date_Of_Joining', models.DateField()),
                ('reporting_To', models.CharField(max_length=100)),
                ('linkedin_Link', models.URLField(max_length=300)),
                ('Photo_File_Name', models.CharField(max_length=100)),
            ],
        ),
    ]
