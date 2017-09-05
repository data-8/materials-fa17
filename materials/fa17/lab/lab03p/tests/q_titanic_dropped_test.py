test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(titanic_dropped) == tables.Table
          True
          >>> titanic_dropped.labels
          ('survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'fare')
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
