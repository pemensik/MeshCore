#!/usr/bin/python
#
# Author: Pihhan <pihhan@gmail.com>
# SPDX-License-Identifier: MIT

import csv
import json

def parse_csv(fname):
    regions = None
    with open(fname, 'r') as f:
         r = csv.reader(f)
         regions = list(r)
    return regions

def process_regions(regions):
    subregions = {}
    rnames = {}
    for i in regions:
         z = i[1].lower()
         if len(z) == 3:
             region = z
             rnames[region] = (i[2], i[3])
             subregions[region] = []
         if len(z) == 2:
             subregions[region].append(z)
             rnames[region] = (i[2], i[3])
    return (subregions, rnames)

def write_json(subregions, fname):
    with open(fname, 'w') as f:
         json.dump(subregions, f)

def print_mesh_regions(subregions, parent = 'cz'):
    for n, v in subregions.items():
        print(f'  region put {n} {parent}')
        for subn in v:
            print(f'  region put {subn} {n}')
        print()

if __name__ == '__main__':
    regions = parse_csv('Regiony.csv')
    (subregions, rnames) = process_regions(regions)
    write_json(subregions, 'Regiony.json')
    print_mesh_regions(subregions)
