import unittest
from config import Config
from app import create_app, db
from app.models import Users


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = Users(username='test')
        u.set_password('test')
        self.assertFalse(u.check_password('false'))
        self.assertTrue(u.check_password('test'))


if __name__ == '__main__':
    unittest.main()
