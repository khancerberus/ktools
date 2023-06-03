import pytest


@pytest.mark.first()
def test_config(app):
    """" Test if the app is configured correctly """
    assert app.testing
    assert not app.debug
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'