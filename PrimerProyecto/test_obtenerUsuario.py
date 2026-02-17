from unittest.mock import patch
from mi_archivo import obtener_usuario

def test_obtener_usuario():
    with patch("builtins.input", return_value="juan"):
        assert obtener_usuario() == "JUAN"

