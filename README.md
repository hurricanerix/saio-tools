SAIO Tools
==========

A collection of dev tools I use working with OpenStack Swift.


Summary of tools
----------------

command | description
------------- | -------------
saio-tools-slo  | Creates static large objects.


saio-tools-slo
--------------
```
$ ./bin/saio-tools-slo --help
usage: saio-tools-slo [-h] [--storage-url STORAGE_URL] [--prefix PREFIX]
                      [--delete-after DELETE_AFTER]
                      [--segment-count SEGMENT_COUNT]
                      [--segment-size SEGMENT_SIZE] [--cleanup] [--verbose]
                      [token]

SAIO Tools Static Large Object Helper.

positional arguments:
  token                 Auth token to use when making requests.If none is
                        provided, the environment variableST_TOKEN will be
                        used.

optional arguments:
  -h, --help            show this help message and exit
  --storage-url STORAGE_URL
                        URL to account to create data in.
  --prefix PREFIX       Container prefix for created containers.
  --delete-after DELETE_AFTER
                        Time in seconds to delete the objects after.If set to
                        0, the "X-Delete-After" header will not be set.
  --segment-count SEGMENT_COUNT
                        Number of segments to create per SLO.
  --segment-size SEGMENT_SIZE
                        Size in bytes to create each segment.
  --cleanup             If set, created containers and objects will be removed
                        before the program terminates.
  --verbose             Show verbose info.
```