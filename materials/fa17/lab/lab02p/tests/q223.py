test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your estimate is a valid year!
          >>> estimate > 1900 and estimate < 2020
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> estimate > 1985
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> estimate > 2000
          True
          """,
          'hidden': False,
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
