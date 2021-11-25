from _utils import TestRunner, TestCase
from question_set_1 import mul_div_main


def main(test_runner: TestRunner):
    test_runner.register(
        test_name="MulDiv",
        test_func=mul_div_main,
        cases=[
            TestCase(([1, 2, 3],), expected=[6., 3., 2.]),
            TestCase(([7, 6, 10, 9, 2],), expected=[1080.0, 1260.0, 756.0, 840.0, 3780.0]),
            TestCase(([99999999999, 2, 999],), expected=[1998.0, 99899999999001.0, 199999999998.0]),
            TestCase(([-1, 777, 21, -33],), expected=[-538461.0, 693.0, 25641.0, -16317.0]),
            TestCase(([33, 33, 33, 99, 9],), expected=[970299.0, 970299.0, 970299.0, 323433.0, 3557763.0]),
            TestCase(([4, 0, 4],), expected=[0., 16., 0.]),
            TestCase(([0, 0, 7],), expected=[0., 0., 0.]),
            TestCase(([1e8, 1e-8, 1+7j, 5e-4+(-99j)],), expected=[6.930005e-06-9.89965e-07j,
                                                                  69300050000-9899650000j,
                                                                  0.0004999999999986926-98.99999999999999j,
                                                                  1+6.999999999999999j]),
            TestCase(([2**32-1, 0, 2**-32+1, 69],), expected=[0., 296352743424.0, 0., 0.]),
            TestCase(([9, 19, -99, 0, 32],), expected=[0., 0., 0., -541728.0, 0.])
        ]
    )
    test_runner.run()
    test_runner.report()


if __name__ == "__main__":
    delim = f"{'-' * 10}"
    runner = TestRunner(delimiter=delim)
    main(runner)
