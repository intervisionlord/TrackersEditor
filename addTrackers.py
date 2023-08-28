# from subprocess import call as call_proc
import re
from subprocess import run as runcommand
import os

trackers_file = 'trackers.txt'
input_dir = ''
output_dir = ''
tracker_list = []

with open(trackers_file, 'r') as f:
    trackers = f.readlines()
    for urls in trackers:
        tracker_list.append(re.sub('\n', '', urls))

torrent_file = input('File: ')

for i in tracker_list:
    # os.exec(f'transmission-edit -a {i} {torrent_file}')
    runcommand([
        'transmission-edit',
        f'-a {i}',
        os.path.abspath(torrent_file)
        ])

print(tracker_list)