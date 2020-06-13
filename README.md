# datasette-psutil

[![PyPI](https://img.shields.io/pypi/v/datasette-psutil.svg)](https://pypi.org/project/datasette-psutil/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-psutil.svg?style=svg)](https://circleci.com/gh/simonw/datasette-psutil)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-psutil/blob/master/LICENSE)

Datasette plugin adding a `/-/psutil` debugging endpoint

## Installation

Install this plugin in the same environment as Datasette.

    $ pip install datasette-psutil

## Usage

Visit `/-/psutil` on your Datasette instance to see various information provided by [psutil](https://psutil.readthedocs.io/).

## Example

You can visit a live demo here: https://datasette-psutil-demo-j7hipcg4aq-uw.a.run.app/-/psutil

Sample output:
```
process.open_files()
  popenfile(path='/tmp/fixtures.db', fd=6)

process.connections()
  pconn(fd=5, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='169.254.8.130', port=8080), raddr=addr(ip='169.254.8.129', port=52621), status='ESTABLISHED')
  pconn(fd=3, family=<AddressFamily.AF_INET: 2>, type=<SocketKind.SOCK_STREAM: 1>, laddr=addr(ip='0.0.0.0', port=8080), raddr=(), status='LISTEN')

process.memory_info()
  pmem(rss=56827904, vms=242540544, shared=0, text=0, lib=0, data=0, dirty=0)

process.cmdline()
  '/usr/local/bin/python'
  '/usr/local/bin/datasette'
  'serve'
  '--host'
  '0.0.0.0'
  '-i'
  'fixtures.db'
  '--cors'
  '--inspect-file'
  'inspect-data.json'
  '--port'
  '8080'

process.parents()
  psutil.Process(pid=1, name='sh', started='23:19:29')

process.threads()
  pthread(id=2, user_time=7.27, system_time=3.99)
  pthread(id=4, user_time=0.01, system_time=0.0)
  pthread(id=5, user_time=0.0, system_time=0.0)
  pthread(id=6, user_time=0.0, system_time=0.0)
  pthread(id=7, user_time=0.0, system_time=0.0)
  pthread(id=8, user_time=0.0, system_time=0.0)

psutil.getloadavg()
  (0.0, 0.0, 0.0)

psutil.cpu_times(True)
  scputimes(user=0.0, nice=0.0, system=0.0, idle=0.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
  scputimes(user=0.0, nice=0.0, system=0.0, idle=0.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)

psutil.virtual_memory()
  svmem(total=2147483648, available=2093080576, percent=2.5, used=31113216, free=2093080576, active=42860544, inactive=11513856, buffers=0, cached=23289856, shared=262144, slab=0)

list(psutil.process_iter())
  psutil.Process(pid=1, name='sh', started='23:19:29')
  psutil.Process(pid=2, name='datasette', started='23:19:29')
```
