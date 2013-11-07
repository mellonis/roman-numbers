from roman import Roman


def test_roman_init():
    assert Roman(5) == 'V'
    assert Roman('IV') == 'IV'
