import datetime
import re
import jinja2
from tcw_tasks.templates import HTML_TEMPLATE, TEXT_TEMPLATE

def test_text_template():
    obj = {
        'name': '123456',
        'title': 'test raffle',
        'instructions': 'add test data',
        'winners': 3,
        'max_entrants': 10,
        'expires': datetime.datetime.now(),
        'attributes': {'winners': ['foo','bar','baz']},
    }
    winners = ['foo','bar','baz']
    msg = jinja2.Template(TEXT_TEMPLATE).render(contest=obj, winners=winners)
    assert re.search('- number of winners: 3', msg)
    assert re.search('1. foo', msg)
    assert re.search('2. bar', msg)
    assert re.search('3. baz', msg)


def test_bad_contest():
    obj = {
        'name': '123456',
        'title': 'test raffle',
        'instructions': 'add test data',
        'winners': 3,
        'max_entrants': 10,
        'expires': datetime.datetime.now(),
        'attributes': None,
    }
    winners = []
    msg = jinja2.Template(TEXT_TEMPLATE).render(contest=obj, winners=winners)
    assert re.search('- number of winners: 0', msg)
