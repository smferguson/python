import argparse
import json
import os
import setproctitle
import subprocess
import time


def Process():
  result = []

  i = 0
  date = {u'timestamp': 1383523200}
  while i < 1462:
    ts = 1383523200
    ms = 86400
    result.append({u'timestamp': ts + (ms * i)})
    i += 1

  f = open(u'dates.json', u'w')
  [f.write(json.dumps(r) + u'\n') for r in result]
  f.close()


if __name__ == '__main__':
  setproctitle.setproctitle(u'Foo')

  exit(Process())
