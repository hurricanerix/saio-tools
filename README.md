SAIO Tools
==========

A collection of dev tools I use working with OpenStack Swift.


Summary of tools
----------------

command | description
------------- | -------------
saio-tools-formpost  | FormPOST objects to Swift.
saio-tools-slo  | Creates static large objects.
saio-tools-txtime | Converts transaction IDs to time formats.
swiftly- | Wrapper for [swiftly](https://github.com/gholt/swiftly) to invoke via configs.


saio-tools-formpost
-------------------
```
$ saio-tools-formpost --help
usage: saio-tools-formpost [-h] [--url URL] [--verbose] [--signature-only]
                           [--boundry BOUNDRY] [--redirect REDIRECT]
                           [--max-file-size MAX_FILE_SIZE]
                           [--max-file-count MAX_FILE_COUNT]
                           [--expires EXPIRES] [--expires-in EXPIRES_IN]
                           [--signature SIGNATURE] [--key KEY] [--version]
                           [files [files ...]]

Swift FormPOST Utility to use the FormPOST feature to POST files to Swift.

positional arguments:
  files                 Files to be posted in the form.

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     URL to post files to.
  --verbose, -v         Print info to stderr.
  --signature-only      Don't POST data, just create a signature.
  --boundry BOUNDRY     Boundry to use in the generated form.
  --redirect REDIRECT, -r REDIRECT
                        Form redirect URL.
  --max-file-size MAX_FILE_SIZE, -s MAX_FILE_SIZE
                        Form max file size.
  --max-file-count MAX_FILE_COUNT, -c MAX_FILE_COUNT
                        Form max file count.
  --expires EXPIRES, -e EXPIRES
                        Form expires timestamp.
  --expires-in EXPIRES_IN
                        Expires in <seconds>, to be converted to the expires
                        timestamp.
  --signature SIGNATURE
                        Form signature to use.
  --key KEY             TempURL key to be used in creating the form signature.
  --version             Show version info.
```

saio-tools-slo
--------------
```
$ saio-tools-slo --help
usage: saio-tools-slo [-h] [--concurrency CONCURRENCY]
                      [--storage-url STORAGE_URL] [--prefix PREFIX]
                      [--delete-after DELETE_AFTER]
                      [--segment-count SEGMENT_COUNT]
                      [--segment-size SEGMENT_SIZE] [--cleanup] [--verbose]
                      [--version]
                      [token]

SAIO Tools Static Large Object Helper.

positional arguments:
  token                 Auth token to use when making requests.If none is
                        provided, the environment variableST_TOKEN will be
                        used.

optional arguments:
  -h, --help            show this help message and exit
  --concurrency CONCURRENCY, -c CONCURRENCY
                        Number of concurrent request to make at a time.
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
  --version             Show version info.
```

saio-tools-txtime
-----------------
```
$ saio-tools-txtime --help
usage: saio-tools-txtime [-h] [--unix] [--version] txid

Converts Swift Transaction IDs to time formats.

positional arguments:
  txid        Auth token to use when making requests.If none is provided, the
              environment variableST_TOKEN will be used.

optional arguments:
  -h, --help  show this help message and exit
  --unix, -u  Display as UNIX timestamp.
  --version   Show version info.
```

swiftly-
--------

Simple wrapper for [swiftly](https://github.com/gholt/swiftly), allowing
credentials to be stored in config files.

Create a config for your SAIO.

```
$ mkdir -p ~/.swift_accounts
$ cat ~/.swift_accounts/saio.config
[keystoneclient]
auth_url=http://127.0.0.1:8080/auth/v1.0
user=test:tester
key=testing
```

Example HEAD request w/ swiftly-

```
$ swiftly- saio head
X-Account-Bytes-Used:                          0
X-Account-Container-Count:                     10
X-Account-Meta-Temp-Url-Key:                   SecretKey
X-Account-Object-Count:                        0
X-Account-Storage-Policy-Gold-Bytes-Used:      0
X-Account-Storage-Policy-Gold-Container-Count: 10
X-Account-Storage-Policy-Gold-Object-Count:    0
X-Timestamp:                                   1429634838.39854
X-Trans-Id:                                    tx215dbf27ac49444c92790-00553e8ffd
```
