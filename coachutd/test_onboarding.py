from coachutd.models import User
from .test import get_test_client
from . import db


def test_onboard():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="Jonathan", password="Hello123"))

        # change description
        response = client.post(
            "/onboarding",
            data=dict(
                age=20,
                sex="male",
                availability="friday,saturday",
                username="Jonathan",
                password="Hello123",
            ),
        )
        assert response.status_code == 200
        assert User.query.filter_by(username="Jonathan").first().age == 20
        assert User.query.filter_by(username="Jonathan").first().sex == "male"
        assert (
            User.query.filter_by(username="Jonathan").first().availability
            == "friday,saturday"
        )
