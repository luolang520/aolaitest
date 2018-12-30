import pytest
class TestAssert:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_a(self):
        assert 2>3,"abc"
    if __name__ == '__main__':
        pytest.main("-s Test_001.py")