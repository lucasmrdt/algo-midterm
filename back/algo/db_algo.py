from typing import List
from datetime import datetime
from functools import total_ordering
from database import select_all_data, RawData
from .hashtable import HashTable
from .priority_queue import PriorityQueue

sorted_array = None
ht_by_year_and_month = None


class RawDataWithIndex:
    def __init__(self, index: int, data: RawData):
        self.index = index
        self.data = data

    def __hash__(self) -> int:
        return self.data.date


@total_ordering
class RawDataOrderedByClosingPrice:
    def __init__(self, data: RawData):
        self.data = data

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, RawDataOrderedByClosingPrice):
            return NotImplemented
        return self.data.closing == o.data.closing

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, RawDataOrderedByClosingPrice):
            return NotImplemented
        return self.data.closing < o.data.closing


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
        return ht_by_year_and_month[date.year][date.month][date.day].data
    except KeyError:
        raise ValueError(f"Date '{date}' not found")


def get_data_between_date(begin: datetime, end: datetime, k=None) -> List[RawData]:
    try:
        begin_index = ht_by_year_and_month[begin.year][begin.month][begin.day].index
    except KeyError:
        begin_index = 0
    try:
        end_index = ht_by_year_and_month[end.year][end.month][end.day].index
    except KeyError:
        end_index = len(sorted_array) - 1
    if k is None:
        return sorted_array[begin_index:end_index + 1]
    return sorted_array[max(begin_index, end_index - k):end_index + 1]


def get_k_best_data_between_date_with_queue(begin: datetime, end: datetime, k: int) -> List[RawData]:
    data = get_data_between_date(begin, end)
    pq = PriorityQueue(k)
    k = min(k, len(data))
    for row in data:
        pq.insert(RawDataOrderedByClosingPrice(row))
    return [pq.pop().data for _ in range(k)]


def get_k_best_data_between_date_with_sort(begin: datetime, end: datetime, k: int) -> List[RawData]:
    data = get_data_between_date(begin, end)
    k = min(k, len(data))
    data = [RawDataOrderedByClosingPrice(row) for row in data]
    from .sort import mergeSort
    mergeSort(data)
    return [d.data for d in data[-k:]]


def query_test_data():
    test_data = select_all_data()
    return [row.content for row in test_data]
