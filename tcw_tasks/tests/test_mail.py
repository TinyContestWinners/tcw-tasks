import os
import datetime
from collections import namedtuple
from tcw_tasks.notify import notify_owner

Contest = namedtuple('Contest',[
    'title',
    'instructions',
    'email',
    'max_entrants',
    'winners',
    'expires',
    'entrants',
    'attributes']
)

def test_local_email():
    contest = Contest(
        'test contest',
        'info',
        'root@localhost',
        10,
        3,
        datetime.datetime.now(),
        ['apple', 'lemon', 'banana', 'mango', 'kiwi', 'lime'],
        {'winners': ['lemon', 'lime', 'mango']}
    )
    winners = ['lemon', 'lime', 'mango']
    assert notify_owner(contest, winners) == None


def test_sendgrid_email():
    os.environ["TCW_MAIL_FROM"] = 'notifications@thecontestkitty.com'
    os.environ["SENDGRID_API_KEY"] = os.getenv('TEST_API_KEY')

    contest = Contest(
        'test contest',
        'info',
        'tinycontestwinners@gmail.com',
        10,
        3,
        datetime.datetime.now(),
        ['apple', 'lemon', 'banana', 'mango', 'kiwi', 'lime'],
        {'winners': ['lemon', 'lime', 'mango']}
    )
    winners = ['lemon', 'lime', 'mango']

    assert notify_owner(contest, winners) == None
