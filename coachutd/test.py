from . import create_app, db

test_app = create_app()
test_app.config.update({
    "TESTING": True,
})

def get_test_client():
    return test_app.test_client()
