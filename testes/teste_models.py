from classes_python.model import DataTable
import pytest


@pytest.fixture
def table():
    return DataTable('A')


def test_add_column(table):
    assert 0 == len(table._columns)

    table.add_column('BId', 'bigint')
    assert 1 == len(table._columns)

    table.add_column('value', 'numeric')
    assert 2 == len(table._columns)

    table.add_column('desc', 'varchar')
    assert 3 == len(table._columns)


def test_add_column_invalid_type(table):
    with pytest.raises(Exception):
        table.add_column('col', 'invalido')


def test_add_relationship(table):
    coluna = table.add_column('BId', 'bigint')
    table_b = DataTable('B')
    table_b.add_column('BId', 'bigint')
    table.add_references = ('B', table, coluna)


def test_add_reverse_relationship(table):
    coluna = table.add_column('BId', 'bigint')
    table_b = DataTable('B')
    coluna = table_b.add_column('BId', 'bigint')
    table_b.add_referenced('A', table, coluna)

    assert 1 == len(table_b.referenced)
    assert 0 == len(table_b.references)





