XCache testing benchmark for 200 Gbps
=====================================


How to Submit
-------------

From coffea.casa, you have to submit with the `-spool` option:

```
condor_submit condor.submit -spool
```

Once complete, you will need to run:

```
condor_transfer_data <jobid>
```


