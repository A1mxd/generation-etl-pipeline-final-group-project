import unittest
import sys
sys.path.append('../src') 
from src.extract_transform import create_item_list

def test_create_itemlist():
    #test with empty input 
    transactions = []
    assert create_item_list(transactions) == []

    #test for single entry
    transactions = [
        {"date": "01/01/2020 10:03",
         "location": "Leeds",
         "name": "Ryan Moye",
         "basket": "Large Filter coffee - 1.80",
         "price": '1.80',
         "payment_method": "CASH"}
    ]
    expected = [
        {"item_name": "Large Filter coffee",
         "item_price": '1.80',
         "temp_transaction_id": 0}
    ]
    assert create_item_list(transactions) == expected

    #test for multiple entries
    transactions = [
        {"date": "01/01/2020 09:22",
         "location": "Leeds",
         "name": "Rudy Joyce",
         "basket": "Large Filter coffee - 1.80, Regular Filter coffee - 1.50, Large Iced americano - 2.50",
         "price": '5.80',
         "payment_method": "CARD",
         "card_number": "4557865396108473"},
        {"date": "01/01/2020 09:27",
         "location": "Leeds",
         "name": "Aaron Cunningham",
         "basket": "Large Filter coffee - 1.80, Large Hot Chocolate - 1.70",
         "price": '3.50',
         "payment_method": "CARD",
         "card_number": "1560104829895802"},
        {"date": "01/01/2020 09:32",
         "location": "Leeds",
         "name": "Joyce Smith",
         "basket": "Large Iced americano - 2.50, Large Iced americano - 2.50",
         "price": '5.00',
         "payment_method": "CASH"}
    ]
    expected = [
        {"item_name": "Large Filter coffee",
         "item_price": '1.80',
         "temp_transaction_id": 0},
        {"item_name": "Regular Filter coffee",
         "item_price": '1.50',
         "temp_transaction_id": 0},
        {"item_name": "Large Iced americano",
         "item_price": '2.50',
         "temp_transaction_id": 0},
        {"item_name": "Large Filter coffee",
         "item_price": '1.80',
         "temp_transaction_id": 1},
        {"item_name": "Large Hot Chocolate",
         "item_price": '1.70',
         "temp_transaction_id": 1},
        {"item_name": "Large Iced americano",
         "item_price": '2.50',
         "temp_transaction_id": 2},
        {"item_name": "Large Iced americano",
         "item_price": '2.50',
         "temp_transaction_id": 2}
    ]
    assert create_item_list(transactions) == expected


