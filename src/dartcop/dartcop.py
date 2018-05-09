#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

VERSION = '0.0.1'

def perror(*args):
  sys.stderr.write(*args)
  sys.stderr.write('\n')

def line2element(string):
  #TODO
  return ''

# Help
def show_help():
  perror('Usage: dartcop [options...] <directory or list of files>')
  perror('       dartcop --version')
  perror('')
  perror('dartcop')
  perror('Homepage: https://github.com/kuronekomichael/dartcop')
  perror('Simple `dartanalyzer` wrapper convert to checkstyle format')
  exit(255)

def main(argv):
  if len(argv) == 0:
    return False

  if argv[0] == '-V' or argv[0] == '--version':
    print('dartcop v' + VERSION)
    exit(0)

  if argv[0] == 'help':
    show_help()
    exit(0)

  #TODO
  exit(1)

if __name__ == '__main__':
  main(sys.argv[1:])