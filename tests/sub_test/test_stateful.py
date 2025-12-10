from hypothesis.stateful import RuleBasedStateMachine, rule
from contracts.sub import stateful
from boa.test.strategies import strategy
from hypothesis import given, settings

class StatefulFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = stateful.deploy()
        
    @rule(new_num=strategy("uint256"))
    def change_num(self, new_num):
        self.contract.change_number(new_num)
        print(f'    Called change_number with {new_num}')
        
    @rule(inp = strategy("uint256"))
    def input_number_returns_itself(self, inp):
        res = self.contract.always_returns_input_number(inp)
        print(f'    Called always_returns with {inp}')
        assert res == inp, f'I caught it mate, Its this number which is troubling us {inp}'
        
TestStatefulFuzzing = StatefulFuzzer.TestCase

TestStatefulFuzzing.settings = settings(max_examples=1000, stateful_step_count=50)