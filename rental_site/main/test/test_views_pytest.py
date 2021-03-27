import pytest
from django.urls import reverse
from main.factories import RegionFactory, GarageFactory, AdFactory, UserFactory


@pytest.mark.django_db
def test_success_index_view(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_apartment_list_view(client):
    url = reverse('apartment_ads')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_room_list_view(client):
    url = reverse('room_ads')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_garage_list_view(client):
    url = reverse('garage_ads')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_land_plot_list_view(client):
    url = reverse('land_plot_ads')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_ad_view(client):
    user = UserFactory()
    region = RegionFactory()
    ad_data = GarageFactory()
    ad = AdFactory(region=region, user=user, content_object=ad_data)
    url = reverse('ad_detail', kwargs={'slug': ad.slug})
    response = client.get(url)
    assert response.status_code == 200


@pytest.fixture
def auto_login_user(db, client):
    def make_auto_login():
        user = UserFactory()
        client.force_login(user)
        return client, user
    return make_auto_login


@pytest.mark.django_db
def test_success_dashboard_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('dashboard')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_realty_list_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('choice_type')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_add_apartment_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('add_apartment')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_add_room_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('add_room')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_add_garage_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('add_garage')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_add_land_plot_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('add_land_plot')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_edit_realty_ad(auto_login_user):
    client, user = auto_login_user()
    region = RegionFactory()
    ad_data = GarageFactory()
    ad = AdFactory(region=region, user=user, content_object=ad_data)
    url = reverse('edit_ad', args=[ad.pk])
    response = client.get(url)
    assert response.status_code == 200
