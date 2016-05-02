Swift Tools
==========

A collection of dev tools I use when working with OpenStack swift.


Summary of tools
----------------

command | description
------------- | -------------
st_expiring_create | Creates lots of expiring objects.
st_expiring_test | Tests that expiring objects are expired.
st_formpost  | FormPOST objects to Swift.
st_slo  | Creates static large objects.
st_txtime | Converts transaction IDs to time formats.
swiftly- | Wrapper for [swiftly](https://github.com/gholt/swiftly) to invoke via configs.


Setup
-----

This is how I set things up:

```
$ mkdir st
$ cd st

$ mkvirtualenv swift

$ git clone git@github.com:hurricanerix/swift-tools.git tools
$ git clone git@github.com:openstack/swift.git
$ git clone git@github.com:openstack/python-swiftclient.git swiftclient
$ git clone git@github.com:gholt/swiftly.git

$ sudo apt-get install xfsprogs python-dev liberasurecode-dev

$ cd swiftclient
$ pip install -r requirements.txt
$ python setup.py devlop
$ cd ..

$ cd swift
$ pip install -r requirements.txt
$ python setup.py devlop
$ cd ..

$ cd swiftly
$ python setup.py devlop
$ cd ..

$ cd tools
$ pip install -r requirements.txt
$ python setup.py devlop
$ cd ..
```
