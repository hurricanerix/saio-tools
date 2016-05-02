Testing Expiring Objects Patch
==============================

Some things to help with testing the expired_objects patch.

https://review.openstack.org/#/c/252085/

Setup
-----

Make sure to:

```Shell
swift-init container-updater start --once
```
after the creation of the first expiring object (to create the .expiring_objects account)

#### tempauth

I am not 100% sure on this, but I think 'account_autocreate' should be set to true
in proxy-server.conf.

#### allow_expired.diff

This diff is used to hack the proxy/object nodes to allow creation of objects with a 'X-Delete-At' header in the past.

To apply it:

```Shell
# TODO: show how to patch.
```

bin/st_create_expired_objects
-----------------------------

Once swift is patched to allow expired objects in the past, this script can be used to create expiring objects within a range.  By default the range contains a majority in the past, with some being in the future.

The only required argument is a valid token.  The most useful optional argument is the count parameter, which allows you to modify the number of objects to create.

The objects created, along with transaction ids and status codes will be written to a log file.

```
$ ./st_create_expired_objects.py AUTH_tk93865e8770814490ba4f2079eb5ef2b7 --count=20
....................

$ cat st_create_expired_objects.log
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/24/19/119f1fc6-1263-464e-aeee-d63503856d76, txe7ac06ea7489443ebec92-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/26/19/ae4253bc-4af1-4418-ace7-f89cb3e3f66e, txccc5ccc168324d0199104-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/05/03/03/d106d7f6-d993-4eb9-a9c9-21bef8051eda, txd909a34e9b774b0dbfea6-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/22/15/2bd35aa6-dcb8-4b0c-9aab-57c12bcce388, txb6dd4b316a694896830d8-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/17/17/c715d663-2c79-44fd-892c-d41652701d75, tx11bac1c30f1b4d2ca6479-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/18/21/050032b7-05b4-42de-938a-2744fdbe6dfd, txdc4e0f096111421da5067-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/29/02/dda48016-9c60-4e46-95b4-08d4c71dd80b, txbc5f385b0013445fa5f40-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/23/20/c496a74a-4901-46c8-bb69-a50d3dcc7a24, tx26146aab739e4633aecd4-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/05/02/10/82a3c06f-8d92-477f-822f-521a761f0ccc, txd04de3f00f0744c697283-0057223fcc, 201
INFO:create_expired_objects:http://127.0.0.1:8080/v1/AUTH_test/test_exp/2016/04/25/15/1b895bf6-b65b-4a2c-8b7e-295d05d46097, tx31595a30400447ffa3293-0057223fcc, 201
```

bin/st_test_expired_objects
---------------------------

Once you have created objects which need to be expired, this script can be used to test how long it takes for all the objects in the past to expire.

TODO: write this tool

```Shell
swift-init object-expirer start
```
