from dashborad.models import Health, Patient
import django_filters


class HealthFilter(django_filters.FilterSet):
    time = django_filters.CharFilter(name='time',lookup_expr='iexact')
    class Meta:
        model = Health
        fields = ['time', 'value']