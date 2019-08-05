# Generated by Django 2.2.4 on 2019-08-05 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=20)),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=100)),
                ('shortName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('problemName', models.CharField(max_length=100)),
                ('shortName', models.CharField(max_length=100)),
                ('problemDetail', models.BinaryField(max_length=10485760)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testInput', models.BinaryField(max_length=131072)),
                ('testOutput', models.BinaryField(max_length=131072)),
                ('onshow', models.BooleanField(default=False)),
                ('md5input', models.CharField(max_length=100)),
                ('md5output', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.User')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.UserRole')),
            ],
            bases=('OnlineJudge.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.User')),
                ('nickname', models.CharField(max_length=20)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Administrator')),
            ],
            bases=('OnlineJudge.user',),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submittime', models.DecimalField(decimal_places=9, max_digits=32)),
                ('submitfile', models.BinaryField(max_length=131072)),
                ('lang', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Language')),
                ('prob', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Problem')),
                ('submitStudent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Student')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='testCases',
            field=models.ManyToManyField(to='OnlineJudge.TestCase'),
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.User')),
            ],
        ),
        migrations.CreateModel(
            name='ContestConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('configRole', models.TextField(max_length=1000)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.User')),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('beginTime', models.DecimalField(decimal_places=9, max_digits=32)),
                ('endTime', models.DecimalField(decimal_places=9, max_digits=32)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.ContestConfig')),
                ('contestproblems', models.ManyToManyField(to='OnlineJudge.Problem')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.User')),
                ('participateCourse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Course')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationAdministrator',
            fields=[
                ('administrator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.Administrator')),
            ],
            bases=('OnlineJudge.administrator',),
        ),
        migrations.CreateModel(
            name='SuperAdministrator',
            fields=[
                ('administrator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.Administrator')),
            ],
            bases=('OnlineJudge.administrator',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagRole', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Administrator')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionStatus',
            fields=[
                ('matter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.Matter')),
                ('status', models.IntegerField()),
                ('result', models.CharField(blank=True, max_length=20)),
                ('judgingMessage', models.CharField(blank=True, max_length=10000)),
                ('aimSubmission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OnlineJudge.Submission')),
            ],
            bases=('OnlineJudge.matter',),
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('matter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.Matter')),
                ('squadName', models.CharField(max_length=100)),
                ('courses', models.ManyToManyField(to='OnlineJudge.Course')),
                ('students', models.ManyToManyField(to='OnlineJudge.Student')),
                ('subOrg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineJudge.Organization')),
            ],
            bases=('OnlineJudge.matter',),
        ),
        migrations.AddField(
            model_name='problem',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Administrator'),
        ),
        migrations.AddField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OnlineJudge.Administrator'),
        ),
        migrations.CreateModel(
            name='GeneralAdministrator',
            fields=[
                ('administrator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='OnlineJudge.Administrator')),
                ('subOrganization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineJudge.Organization')),
            ],
            bases=('OnlineJudge.administrator',),
        ),
    ]
