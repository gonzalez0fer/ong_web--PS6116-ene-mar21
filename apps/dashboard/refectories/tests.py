from django.urls import reverse, resolve
from django.test import RequestFactory
from mixer.backend.django import mixer
from apps.main.refectories.models import Refectory
from apps.main.users.models import CustomUser
from apps.main.water_tanks.models import WaterTank
from .views import RefectoryUpdateView
import pytest

class TestUrls:
    def test_list_url(self):
        path = reverse ('dashboard:refectory:list_refectories')
        assert resolve(path).view_name == 'dashboard:refectories:list_refectories'

    def test_create_url(self):
        path = reverse ('dashboard:refectory:create_refectory')
        assert resolve(path).view_name == 'dashboard:refectories:create_refectory'

    def test_edit_url(self):
        path = reverse ('dashboard:refectory:edit_refectory', kwargs={'pk': 1})
        assert resolve(path).view_name == 'dashboard:refectories:edit_refectory'

@pytest.mark.django_db
class TestModels:
    def test_refectory_model(self):
        user = mixer.blend(CustomUser)
        refectory = mixer.blend(Refectory, created_by=user)
        assert Refectory.objects.get(id=1).name == refectory.name

@pytest.mark.django_db
class TestViews:
    def test_update_view(self):
        user = mixer.blend(CustomUser)
        refectory = mixer.blend(Refectory, created_by=user)
        water_tank = mixer.blend(WaterTank, refectory=refectory, created_by=user, current_liters=10, capacity=100)
        print(refectory.__dict__)
        path = reverse('dashboard:refectory:edit_refectory', kwargs={'pk': refectory.id})
        request = RequestFactory().get(path)
        response = RefectoryUpdateView.as_view()(request,pk=refectory.id)
        assert response.status_code == 200

