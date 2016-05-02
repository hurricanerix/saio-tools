#!/usr/bin/env python
from __future__ import print_function

import argparse
import datetime
import calendar
import uuid
import random
import logging
import sys

import eventlet
from eventlet.green import urllib2


def _get_date(offset):
    today = datetime.date.today()
    d = today + datetime.timedelta(days=offset)
    return calendar.timegm(d.timetuple())


def _get_delete_at(start, end):
    return random.randint(start, end)


def _get_urls(token, container, count, start_date=None, end_date=None):
    for _ in xrange(count):
        delete_at = None
        if start_date and end_date:
            delete_at = _get_delete_at(start_date, end_date)
        prefix = datetime.datetime.fromtimestamp(
            delete_at).strftime('%Y/%m/%d/%H')
        object_name = '{prefix}/{id}'.format(prefix=prefix, id=uuid.uuid4())
        url = 'http://127.0.0.1:8080/v1/AUTH_test/{0}/{1}'.format(
            container, object_name)
        yield {'token': token, 'url': url, 'delete_at': delete_at}


def create_objects(data):
    # TODO: handle errors
    url = data.get('url')
    token = data.get('token')
    delete_at = data.get('delete_at')

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url, data='')
    request.add_header('Content-Type', 'text/plain')
    request.add_header('X-Auth-Token', token)
    request.add_header('X-Delete-At', delete_at)
    request.get_method = lambda: 'PUT'
    result = opener.open(request)

    txid = result.headers.getheader('X-Trans-Id')
    status = result.getcode()

    return url, txid, status


def main(logger):
    parser = argparse.ArgumentParser(
        description='create some object to expire')
    parser.add_argument('--start-date', default=_get_date(-14))
    parser.add_argument('--end-date', default=_get_date(7))
    parser.add_argument('--count', type=int, default=10)
    parser.add_argument('--container', default='test_exp')
    parser.add_argument('token', default=None)

    args = parser.parse_args()
    urls = _get_urls(
            args.token, args.container, args.count, args.start_date,
            args.end_date)

    pool = eventlet.GreenPool(20)
    for url, txid, status in pool.imap(create_objects, urls):
        print('.', file=sys.stdout, end='')
        logger.info('{0}, {1}, {2}'.format(url, txid, status))
    print('')


if __name__ == '__main__':
    logging.basicConfig(filename='create_expired_objects.log',
                        level=logging.INFO)
    logger = logging.getLogger('create_expired_objects')
    main(logger)
