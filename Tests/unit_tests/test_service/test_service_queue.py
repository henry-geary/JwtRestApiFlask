import fakeredis
import pytest
from Services import queue as q


r_fake = fakeredis.FakeStrictRedis(version=6)


def test_push_fakeredis(key, msg):
    q.push_redis(r_fake,key,msg)
    r_fake.lpush(key, msg)
    size = r_fake.llen(key)
    msg = r_fake.lindex(key, size - 1)
    assert msg == b'Buenos dias'


def test_pop_fakeredis(key, msg):
    r_fake.lpush(key, msg)
    assert q.pop_redis(r_fake, key) == 'Buenos dias'


def test_count_fakeredis(key):
    assert q.count_redis(r_fake, key) == r_fake.llen(key)


if __name__ == "__main__":
    pytest.main()