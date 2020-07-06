from dashborad.models import Health, Patient
import django_filters


class HealthFilter(django_filters.FilterSet):
    class Meta:
        model = Health
        fields = ['time', 'value']