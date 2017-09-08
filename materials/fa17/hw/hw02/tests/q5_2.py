test = {
  'name': 'Question 5_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(cumulative_sum_answer) == int
          True
          >>> 1 <= cumulative_sum_answer <= 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> cumulative_sum_answer == 2
          True
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
