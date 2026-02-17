from esPrimo import esPrimo

def test_noEsPrimo():
    output = esPrimo(15)
    assert output == False

def test_esPrimo():
    output = esPrimo(29)
    assert output == True
    
import pytest

@pytest.mark.parametrize("numero,resultado", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (25, False),
    (97, True),
])
def test_es_primo(numero, resultado):
    assert esPrimo(numero) == resultado