test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from datascience import *
          >>> # Make sure change_table is a table
          >>> type(change_table) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you're using the correct arrays!
          >>> change_table.column("Year").item(0) == 1950
          True
          >>> change_table.column("Change").item(0) == 37311223
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
