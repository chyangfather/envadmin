#!/usr/bin/env python
import time
import cli.log

@cli.log.LoggingApp
def sleep(app):
    app.log.log("About to sleep for %d seconds"%app.params.seconds)
    time.sleep(app.params.seconds)

sleep.add_param("seconds",help="time to sleep",default=1,type=int)
if __name__=="__main__":
    sleep.run()
