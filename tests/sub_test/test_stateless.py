import pytest
from contracts.sub import stateless
from hypothesis import given, settings
from boa.test.strategies import strategy

@settings(max_examples=100000)
@given(inp=strategy("uint256"))
def test_always_input(inp):
    '''
    for inp in range(100000):
        assert contract.always_returns_input_number(inp) == inp
        
    This also works, but it takes lot of time, iterating over every case order wise
    '''
    
    contract = stateless.deploy()
    assert contract.always_returns_input_number(inp) == inp
    print(inp)