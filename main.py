"""
Earthquake detection app:
Modularization with Function,
Modularization with Package

Manual input version
"""
from test_eq_manual_scrap1 import data_extract, show_data

if __name__ == '__main__':
    print('Main App\n')
    result = data_extract()
    show_data(result)