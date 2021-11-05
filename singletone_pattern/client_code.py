"""Таким образом, мы видим, что база данных будет создана только одна"""
from singletone_pattern.data_base import DataBase


if __name__ == "__main__":
    db = DataBase(value="DataBase first")
    db_2 = DataBase(value="DataBase second")
    print(db.select())
    print(db_2.select())
