'''
Just make sure the data can be loaded on all supported Python versions.
'''

def test_load_gapminder():
    from gapminder import gapminder
    assert gapminder.iloc[0, 0] == 'Afghanistan'

