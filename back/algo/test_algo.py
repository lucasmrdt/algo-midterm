from database import get_all_content_of_test


def query_test_data():
    test_data = get_all_content_of_test()
    return [row.content for row in test_data]
