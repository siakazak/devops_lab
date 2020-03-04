#!/bin/env python

import requests
import argparse
import getpass

rj = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=('flyboy14', 'dwarfmanoo89')).json()

# for i in range(len(rj)):
# 	print(str(i + 1) + '. ' + rj[i]['title'])
print(rj)
