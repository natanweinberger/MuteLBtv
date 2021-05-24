import pytest
from datetime import datetime
from game import convert_datetime_to_timecode


@pytest.mark.parametrize("dt, expected", [
    (datetime(2021, 1, 1, 9, 0, 0), '20210101_090000'),
    (datetime(2021, 10, 20, 9, 0, 0), '20211020_090000'),
    (datetime(2021, 10, 20, 13, 30, 15), '20211020_133015'),
])
def test_convert_datetime_to_timecode(dt, expected):
    ret = convert_datetime_to_timecode(dt)
    assert ret == expected
