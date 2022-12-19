import pytest
import datetime
from tcw.config import Development
from tcw.database import init_db, session
from tcw.apps.contest.models import Contest, Entrant
from tcw.utils import expires_time
from tcw_tasks.utils import expired_contests


@pytest.fixture
def db():
    init_db('sqlite://')


@pytest.fixture
def contests():
    # create 5 contests. 2 expired, 3 active
    for i in [-2, -1, 1, 2, 3, 4]:
        c = Contest(
            name="random-%d" % i,
            title="contest %d" % i,
            instructions="instructions %d" % i,
            max_entrants=10,
            winners=5,
            expires=expires_time(i))
        session.add(c)
    session.commit()


@pytest.fixture
def entries():
    contests = session.query(Contest).all()

    # fill the entrants of the last contest
    cid = contests[-1].id
    for i in range(1, contests[-1].max_entrants + 1):
        name = "entrant-name-%d" % i
        e = Entrant(name=name, contest_id=cid)
        session.add(e)

    # add some entrants, but not fill it, in another contest
    cid = contests[-2].id
    for i in range(1, contests[-2].max_entrants):
        name = "entrant-name-%d" % i
        e = Entrant(name=name, contest_id=cid)
        session.add(e)

    session.commit()


def test_init(db):
    assert session is not None


def test_contest(contests):
    results = session.query(Contest).all()
    assert len(results) == 6


def test_entrants(entries):
    contests = session.query(Contest).all()
    assert len(contests[-1].entrants) == contests[-1].max_entrants
    assert len(contests[-2].entrants) == (contests[-2].max_entrants - 1)


def test_expired():
    results = expired_contests()
    # two are expired times, one is expired because max entrants
    assert len(results) == 3
