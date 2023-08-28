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
    torrents_list.append(os.path.join(os.path.abspath(torrents_dir), os.path.basename(files)))
    # print(os.path.abspath(f'{torrents_dir}\{files}'))
    # print(f'{os.path.abspath(torrents_dir)}\{os.path.basename(files)}')
print(torrents_list)

# print(torrents_list)

for torrent in torrents_list:
    for url in tracker_list:
        print(f'trying to edit {torrent}')
        runcommand([
            'transmission-edit',
            f'-a {url}',
            f'{torrent}',
            ])