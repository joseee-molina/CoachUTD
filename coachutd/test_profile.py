from coachutd.models import User
from .test import get_test_client
from . import db

def test_change_description():
    client = get_test_client()

    with client.application.app_context():
        # create a user
        db.session.add(User(username="test", password="test"))

        # change description
        response = client.post('/about', data=dict(about="new about", username="test", password="test"))
        assert response.status_code == 200
        assert User.query.filter_by(username="test").first().about == "new about"

