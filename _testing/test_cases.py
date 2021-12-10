from _testing.utils import TestCase


muldiv_test_cases = [
    TestCase(([1, 2, 3],), expected=[6., 3., 2.]),
    TestCase(([7, 6, 10, 9, 2],), expected=[1080.0, 1260.0, 756.0, 840.0, 3780.0]),
    TestCase(([99999999999, 2, 999],), expected=[1998.0, 99899999999001.0, 199999999998.0]),
    TestCase(([-1, 777, 21, -33],), expected=[-538461.0, 693.0, 25641.0, -16317.0]),
    TestCase(([33, 33, 33, 99, 9],), expected=[970299.0, 970299.0, 970299.0, 323433.0, 3557763.0]),
    TestCase(([4, 0, 4],), expected=[0., 16., 0.]),
    TestCase(([0, 0, 7],), expected=[0., 0., 0.]),
    TestCase(([1e8, 1e-8, 1 + 7j, 5e-4 + (-99j)],), expected=[6.930005e-06 - 9.89965e-07j,
                                                              69300050000 - 9899650000j,
                                                              0.0004999999999986926 - 98.99999999999999j,
                                                              1 + 6.999999999999999j]),
    TestCase(([2 ** 32 - 1, 0, 2 ** -32 + 1, 69],), expected=[0., 296352743424.0, 0., 0.]),
    TestCase(([9, 19, -99, 0, 32],), expected=[0., 0., 0., -541728.0, 0.])
]

bitmask_test_cases = [
    TestCase((0x0,), expected={0x0, }),
    TestCase((2 ** 10 - 1,), expected=set(x for x in range(2 ** 10))),
    TestCase((312,), expected={0, 8, 16, 24, 32, 40, 48, 56, 256, 264, 272, 280, 288, 296, 304, 312}),
    TestCase((1,), expected={0, 1}),
    TestCase((12,), expected={0, 4, 8, 12}),
    TestCase((542,), expected={0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 512, 514,
                               516, 518, 520, 522, 524, 526, 528, 530, 532, 534, 536, 538, 540, 542})
]

raincatcher_test_cases = [
    TestCase(([3, 5, 1, 4],), expected=3),
    TestCase(([6, 3, 8, 1, 5, 2, 3],), expected=8),
    TestCase(([1, 2, 3, 4, 5, 6],), expected=0),
    TestCase(([1, 4, 2, 5, 4, 2],), expected=2),
    TestCase(([3, 2, 3, 4, 5, 7, 6, 3, 1, 2],), expected=2),
    TestCase(([8, 1, 1, 2, 1, 3, 999],), expected=32),
    TestCase(([5, 6, 2, 1, 4, 3, 1, 3, 2, 2],), expected=7),
    TestCase(([3, 3, 3, 3, 3, 3, 3],), expected=0),
    TestCase(([7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],), expected=0),
    TestCase(([99999, 1, 1, 0, 2, 1, 99999],), expected=1),
]

find_pos_neg_test_cases = [
    TestCase(([-4, -3, 2, 1, -1, -2, 3, 4],), expected=[2, 1, 3, 4]),
    TestCase(([0, -1, 7, 5, 3, 1, 4, -8, -2],), expected=[1]),
    TestCase(([7, 9, 0, 9, 8, 1, 9, 3, 0, -9],), expected=[9, 9, 9]),
    TestCase(([1, 9, 2, 8, -3, -7, 5, 2, 1, 6, -10],), expected=[]),
    TestCase(([],), expected=[]),
    TestCase(([-9, -2, -4, -8, -3, 1, 3],), expected=[3])
]


dict_tree_search_cases = [
    TestCase(({}, None), expected=(1, 0, 0, 0)),
    TestCase((
        {
            'name': 'Georgi',
            'age': 25,
            'occupation': {
                'title': 'Software Developer',
                'company': 'Acronis'
            }
        }, 'Acronis'), expected=(2, 3, 1, 1)),
    TestCase((
        {
            'car': {
                'make': 'BMW',
                'model': 'M8',
                'year': 2019,
                'engine': {
                    'manufacturer': 'bmw',
                    'horsepower': 625,
                    'capacity_L': 4.4,
                    'cylinders': 8,
                    'fuel_consumption': {
                        'type': 'petrol',
                        'urban': 15.2,
                        'x_urban': 7.8,
                        'combined': 10.5
                    }
                },
                'gears': [1, 2, 3, 4, 5, 6, 'R'],
                'approved_resellers': ['bmw', 'bmw_group']
            }
        }, 'BMW'), expected=(4, 7, 13, 4)),
    TestCase((
        {
            'movies': [
                {
                    'name': 'The Jungle Book',
                    'director': 'Wolfgang Reitherman',
                    'writers': ['Larry Clemmons', 'Ralph Wright', 'Ken Anderson'],
                    'year': 1967,
                    'genres': ['Animation', 'Adventure', 'Comedy'],
                    'stars': [
                        {
                            'name': 'Phil Harris',
                            'age': 63,
                            'character': 'Baloo',
                        },
                        {
                            'name': 'Sebastian Cabot',
                            'age': 49,
                            'character': 'Bagheera',
                        },
                        {
                            'name': 'Louis Prima',
                            'age': 57,
                            'character': 'King Louie of the Apes',
                        }
                    ]
                },
                {
                    'name': 'Your Name',
                    'director': 'Makoto Shinkai',
                    'writers': ['Makoto Shinkai'],
                    'year': 2016,
                    'genres': ['Animation', 'Drama', 'Fantasy'],
                    'stars': [
                        {
                            'name': 'Ryûnosuke Kamiki',
                            'age': 23,
                            'character': 'Taki Tachibana',
                        },
                        {
                            'name': 'Mone Kamishiraishi',
                            'age': 18,
                            'character': 'Mitsuha Miyamizu',
                        }
                    ]
                },
                {
                    'name': 'The Green Mile',
                    'director': 'Frank Darabont',
                    'writers': ['Stephen King', 'Frank Darabont'],
                    'year': 1999,
                    'genres': ['Crime', 'Drama', 'Fantasy'],
                    'stars': [
                        {
                            'name': 'Tom Hanks',
                            'age': 43,
                            'character': 'Paul Edgecomb',
                        },
                        {
                            'name': 'Michael Clarke Duncan',
                            'age': 42,
                            'character': 'John Coffey',
                        },
                        {
                            'name': 'David Morse',
                            'age': 46,
                            'character': 'Brutus Howell',
                        }
                    ]
                }
            ]
         }, 'Animation'), expected=(5, 37, 11, 2)),
    TestCase((
        {
            'cpu_metrics': {
                'file_servers': [55.1, 82.1, 0.01, 100., 0.03, 91.1, 100.],
                'app_servers': [21., 25., 11., 99.9, 45.2, 12.1, 0.1],
                'dbs': [99.9, 100., 100.]
            },
            'memory_metrics': {
                'file_servers': [87.2, 100., 0.04, 100., 1.1, 100., 100.],
                'app_servers': [65., 53., 61.1, 87.7, 49.4, 32.9, 0.02],
                'dbs': [83.91, 97.2, 100.]
            }
        }, 100.), expected=(3, 0, 34, 9))
]
