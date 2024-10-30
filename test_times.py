from times import time_range, compute_overlap_time
import pytest
import yaml


with open('fixture.yaml', 'r') as f:
    test_cases = yaml.safe_load(f)

in_and_out=[]

for a in test_cases:
    expected = []
    for i in test_cases[a]["expected"]:
        x = tuple(i)
        expected.append(x)
    in_and_out.append(((time_range(*test_cases[a]["time_range_1"]),time_range(*test_cases[a]["time_range_2"])),expected))


    
@pytest.mark.parametrize("test_input,expected", in_and_out)
def test_compute_overlap_time(test_input, expected):
    assert compute_overlap_time(*test_input) == expected

