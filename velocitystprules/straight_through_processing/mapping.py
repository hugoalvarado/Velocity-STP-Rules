RULESET_MAP = {
    # This is a dictionary where each key is a tuple with the date, state, line and policy type name,
    # and the value the name of a py file with 'rules' that are defined for the policy type

    # SAMPLE LED: 2018-10-24
    ('2018-10-24', 'State1', 'Homeowners', 'Homeowners Policy'): 'homeowners_10_24_2018',
    ('2018-10-24', 'State2', 'Businessowners', 'Businessowners Policy'): 'businessowners_10_24_2018',

    # SAMPLE LED: 2018-10-25
    # ('2018-10-25', 'State1', 'Homeowners', 'Homeowners Policy'): 'homeowners_10_25_2018',
    # ('2018-10-25', 'State2', 'Businessowners', 'Businessowners Policy'): 'businessowners_10_25_2018',
    # ...
}
