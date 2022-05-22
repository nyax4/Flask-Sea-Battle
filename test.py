import unittest, os
from app import app, db
from app.models import User

class UserModelCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()

        db.create_all()
        u1 = User(username='testUser_0', email='testuser0@testmail.com', wins_count=9, lost_count=24)
        u1.set_password("testuserpassword0")
        u2 = User(username='testUser_1', email='testuser1@testmail.com', wins_count=1, lost_count=0)
        u1.set_password('testuserpassword1')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
    
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        return super().tearDown()
    
    def test_is_committed(self):
        u = User.query.all()
        for v in u:
            if v.username == 'testUser_0':
                self.assertNotEqual(v.username, 'testUser_1')
        db.session.flush()
        db.session.commit()
        

if __name__ =='__main__':
    unittest.main()