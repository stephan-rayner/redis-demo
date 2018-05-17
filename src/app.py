"""This is a demo of using python, redis, and docker"""
import redis
from time import sleep


def main():
    """Everyone loves main functions and my linter made me write a doc string"""
    
    # both of these options work slightly differently.
    # r = redis.StrictRedis(host='redis', port=6379)
    r = redis.Redis(host='redis', port=6379)

    r.set('foo', 'bar')
    r.set('cheese', 'doodle')

    # The decode is because redis returns bytes and I want a utf-8 string.
    hopefully_doodle = r.get('cheese').decode('utf-8')

    print("They value for the key cheese is {}".format(hopefully_doodle))
    sleep(1)

if __name__ == '__main__':
    main()
    