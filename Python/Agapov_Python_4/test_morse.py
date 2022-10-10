from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [
        ('.... . .-.. .-.. ---', 'HELLO'),
        ('.-.-.-', '.'),
        ('', ''),
    ],
)
def test_count_letters(source_string, result):
    assert decode(source_string) == result
