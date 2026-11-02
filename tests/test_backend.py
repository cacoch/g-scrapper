import pytest
from  backend import dict2csv





def test_dict2csv():
    result = """key1,key2
aaa,bbb
ccc,ddd
"""
    data = [{"key1": "aaa", "key2" : "bbb"},
            {"key1": "ccc", "key2" : "ddd"}]

    assert dict2csv(data) == result
