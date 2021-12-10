from _testing.test_cases import (
    bitmask_test_cases, muldiv_test_cases, raincatcher_test_cases, find_pos_neg_test_cases,
    dict_tree_search_cases
)
from _testing.utils import TestRunner
from question_set_1 import mul_div, bit_masks
from question_set_2 import rain_catcher
from question_set_3 import find_pos_neg_couples, dict_search


def main(test_runner: TestRunner):
    test_runner.register(
        test_name="MulDiv",
        test_func=mul_div,
        cases=muldiv_test_cases
    )

    test_runner.register(
        test_name='BitMasks',
        test_func=bit_masks,
        cases=bitmask_test_cases
    )

    test_runner.register(
        test_name='RainCatcher',
        test_func=rain_catcher,
        cases=raincatcher_test_cases
    )

    test_runner.register(
        test_name='PosNegFinder',
        test_func=find_pos_neg_couples,
        cases=find_pos_neg_test_cases
    )

    test_runner.register(
        test_name='DictionaryTreeSearch',
        test_func=dict_search,
        cases=dict_tree_search_cases
    )

    test_runner.run()
    test_runner.report()


if __name__ == "__main__":
    delim = f"{'-' * 10}"
    runner = TestRunner(delimiter=delim)
    main(runner)
