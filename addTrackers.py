# from subprocess import call as call_proc
import re
from subprocess import run as runcommand
import os
from sys import argv

trackers_file = 'trackers.txt'
torrents_dir = argv[1]
tracker_list = []
torrents_list = []

with open(trackers_file, 'r') as f:
    trackers = f.readlines()
    for urls in trackers:
        tracker_list.append(re.sub('\n', '', urls))

for files in os.listdir(torrents_dir):
    torrents_list.append(os.path.abspath(files))

print(torrents_list)

for torrent in torrents_list:
    for url in tracker_list:
        print(f'trying to edit {(torrent)}')
        runcommand([
            'transmission-edit',
            f'-a {url}',
            torrent,
            ])