"""Таким образом, мы видим, что база данных будет создана только одна."""
from patterns.singletone.base_singletone import DataBase

if __name__ == "__main__":
    db = DataBase(value="DataBase first")
    db_2 = DataBase(value="DataBase second")
    print(db.select())
    print(db_2.select())
