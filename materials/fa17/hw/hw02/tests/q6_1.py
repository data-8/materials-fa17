test = {
  'name': 'Question 6_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hint: shortest is a number between 40 and 50.
          >>> 40 <= shortest <= 50
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: longest is a number between 70 and 130.
          >>> 70 <= longest <= 130
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: the average is between the shortest and the longest
          >>> shortest <= average <= longest
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: shortest is a number between 40 and 50.
          >>> shortest
          43
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: longest is a number between 70 and 130.
          >>> longest
          96
          """,
          'hidden': True,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: the average is between the shortest and the longest
          >>> np.isclose(average, 70.8970588235)
          True
          """,
          'hidden': True,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
