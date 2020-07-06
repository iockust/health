from dashborad.models import Health, Patient
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['username', 'first_name', 'last_name', ]