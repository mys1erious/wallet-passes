import pytest
from wallet_pass.main import first_test


def test_first_test():
    assert first_test() == 'first test'
