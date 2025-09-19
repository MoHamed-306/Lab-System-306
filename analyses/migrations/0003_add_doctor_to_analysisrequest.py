from django.db import migrations, models
import django.db.models.deletion


def populate_doctor(apps, schema_editor):
    AnalysisRequest = apps.get_model('analyses', 'AnalysisRequest')
    for ar in AnalysisRequest.objects.select_related('patient__doctor').filter(doctor__isnull=True):
        try:
            ar.doctor = ar.patient.doctor
            ar.save(update_fields=['doctor'])
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0002_alter_analysis_options_alter_analysisrequest_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisrequest',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='analysis_requests', to='patients.doctor', verbose_name='الدكتور'),
        ),
        migrations.RunPython(populate_doctor, reverse_code=migrations.RunPython.noop),
    ]
