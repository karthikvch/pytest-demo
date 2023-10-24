# test_capitalize.py

def capital_case(x):
    return x.capitalize()


def test_capital_case():
    x = capital_case('semaphore')
    assert x == 'Semaphore'
