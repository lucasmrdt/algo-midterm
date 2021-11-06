from typing import List
from datetime import datetime
from database import select_all_data, RawData
from .hashtable import HashTable

sorted_array = None
ht_by_year_and_month = None


class RawDataWithIndex:
    def __init__(self, index: int, data: RawData):
        self.index = index
        self.data = data

    def __hash__(self) -> int:
        return self.data.date


def create_hashtable_by_year(data: List[RawData]):
    # creating
    min_year = data[0].date.year
    max_year = data[-1].date.year
    nb_years = max_year - min_year + 1
    ht = HashTable(size=nb_years)

    for y in range(nb_years):
        year_ht = HashTable(size=12)
        for m in range(12):
            month_ht = HashTable(size=31)
            year_ht[1 + m] = month_ht
        ht[min_year + y] = year_ht

    # fill
    for i, row in enumerate(data):
        ht[row.date.year][row.date.month][row.date.day] = RawDataWithIndex(
            i, row)

    # stats
    nb_collisions = 0
    nb_buckets = 0

    nb_collisions += ht.getNbCollisions()
    nb_buckets += ht.size
    for _, y_ht in ht.iter():
        nb_collisions += y_ht.getNbCollisions()
        nb_buckets += y_ht.size
        for _, m_ht in y_ht.iter():
            nb_collisions += m_ht.getNbCollisions()
            nb_buckets += m_ht.size
    print(f"Number of collisions in hashtable: {nb_collisions}/{nb_buckets}")

    return ht


def init_algo():
    global ht_by_year_and_month, sorted_array
    sorted_array = sorted(select_all_data())
    ht_by_year_and_month = create_hashtable_by_year(sorted_array)


def get_data_by_date(date: datetime) -> RawData:
    try:
        return [ht_by_year_and_month[date.year][date.month][date.day].data.serealize()]
    except TypeError:
        raise ValueError(f"Date '{date}' not found")


def get_data_between_date(begin: datetime, end: datetime, k: int) -> List[RawData]:
    try:
        begin_index = ht_by_year_and_month[begin.year][begin.month][begin.day].index
    except TypeError:
        begin_index = 0
    try:
        end_index = ht_by_year_and_month[end.year][end.month][end.day].index
    except TypeError:
        end_index = len(sorted_array) - 1
    return [sorted_array[i].serealize() for i in range(max(begin_index, end_index - k), end_index + 1)]


def query_test_data():
    test_data = select_all_data()
    return [row.content for row in test_data]
