from typing import List
from datetime import datetime
from database import select_all_data, RawData
from .hashtable import HashTable
from .bst import BST

data: List[RawData] = None
ht = HashTable()
bst = BST()


def init_algo():
    global data
    data = sorted(select_all_data())
    for row in data:
        ht[row.date] = row
    bst.fromSortedArray(data)


def get_data_by_date(date: datetime) -> RawData:
    return ht[date].serealize()


def query_test_data():
    test_data = select_all_data()
    return [row.content for row in test_data]
