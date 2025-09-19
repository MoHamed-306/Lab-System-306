from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from patients.models import Patient
from analyses.models import Analysis

@receiver(post_save, sender=User)
def set_default_permissions(sender, instance, created, **kwargs):
    if created:
        # إعطاء صلاحيات المرضى والتحاليل تلقائياً
        perms = Permission.objects.filter(content_type__app_label__in=['patients', 'analyses'])
        instance.user_permissions.set(perms)
        instance.is_staff = True
        instance.save()
        # تصفير بيانات المرضى والتحاليل لهذا المستخدم الجديد
        Patient.objects.filter(user=instance).delete()
        Analysis.objects.filter(user=instance).delete()
