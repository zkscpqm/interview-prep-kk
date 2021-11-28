from typing import Dict, Any, Callable, List, Union


class TermColour:

    _RED: str = '\033[91m'
    _YELLOW: str = '\033[93m'
    _GREEN: str = '\033[92m'
    _RESET: str = '\033[0m'

    _BOLD: str = '\033[1m'

    @classmethod
    def error(cls, log: str) -> str:
        return f'{cls._RED}{log}{cls._RESET}'

    @classmethod
    def info(cls, log: str) -> str:
        return f'{cls._YELLOW}{log}{cls._RESET}'

    @classmethod
    def ok(cls, log: str) -> str:
        return f'{cls._GREEN}{log}{cls._RESET}'


class TestCase:

    def __init__(self, inp_args: tuple = None, inp_kwargs: dict = None, expected: Any = None):
        self.inp_args: tuple = inp_args or ()
        self.inp_kwargs: dict = inp_kwargs or {}
        self.expected: Any = expected


class RunnableTest:

    def __init__(self, name: str, func: Callable):
        self.name: str = name
        self._func: Callable = func

    def execute(self, *args, **kwargs):
        return self._func(*args, **kwargs)

    def __eq__(self, other: 'RunnableTest') -> bool:
        return self.name == other.name and self._func == other._func

    def __hash__(self) -> int:
        return hash(self.name) + hash(self._func)


class TestRunner:

    def __init__(self, delimiter: str, tests: Dict[RunnableTest, List[TestCase]] = None):
        self.delimiter: str = delimiter
        self.tests: Dict[RunnableTest, List[TestCase]] = tests or {}
        self._curr_test: Union[RunnableTest, None] = None
        self._curr_case: Union[TestCase, None] = None
        self._curr_exc: Union[Exception, None] = None
        self.results: Dict[str, float] = {}

    def register(self, test_name: str, test_func: Callable, cases: List[TestCase]):
        self.tests[RunnableTest(name=test_name, func=test_func)] = cases

    def report(self):
        if len(self.results) == 0:
            print("Nothing to report...")
            return
        rv = f"\nREPORT:\n{self.delimiter}\n\n"
        for test_name, test_result in self.results.items():
            rv += f'{test_name} % pass: {test_result:.2f}%\n'

        print(TermColour.info(rv))

    def _format_args(self, *args, **kwargs) -> str:
        rv = ''

        if len(args) > 0:
            rv += f"Args: {', '.join((str(x) for x in (args or self._curr_case.inp_args)))}\n"

        if len(kwargs) > 0:
            rv += f"Kwargs: {', '.join((f'{k}={v}' for k, v in (kwargs.items() or self._curr_case.inp_kwargs.items())))}"

        return rv

    def run(self):
        print("--- TEST START ---\n")

        for test, cases in self.tests.items():
            print(self.delimiter)
            print(f"Running tests for: {test.name}")
            self._curr_test = test
            case_num = 1
            passed = 0
            for case in cases:
                self._curr_case = case
                self._curr_exc = None
                print(self.delimiter)
                try:
                    actual = test.execute(*case.inp_args, **case.inp_kwargs)
                except Exception as e:
                    self._curr_exc = e
                    actual = f"EXCEPTION RAISED: {self._curr_exc}"
                if case.expected == actual:
                    print(TermColour.ok(f"[{test.name}][{case_num}] Passed!"))
                    passed += 1
                else:
                    print(f"{TermColour.error(f'[{test.name}][{case_num}] Failed!!')}\n"
                          f"Called with: {self._format_args(*case.inp_args, **case.inp_kwargs)}"
                          f"Expected: {case.expected}\n"
                          f"Actual: {actual}")
                case_num += 1
            self.results[test.name] = (passed / (case_num - 1)) * 100
