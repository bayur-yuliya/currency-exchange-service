import pytest
from django.test import RequestFactory

from exchange.views import main_view


@pytest.mark.django_db
def test_main_view_records():
    factory = RequestFactory()
    request = factory.get("/")

    response = main_view(request)

    assert response.status_code == 200