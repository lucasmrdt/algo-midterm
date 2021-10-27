from .models import Test
from .db import db


def get_all_content_of_test():
    return Test.query.all()


def import_test_data():
    test_data = [
        Test(content="test1"),
        Test(content="test2"),
        Test(content="test3")]
    for test in test_data:
        db.session.add(test)
    db.session.commit()
