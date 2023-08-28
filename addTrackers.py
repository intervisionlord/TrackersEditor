import re
import os
from sys import argv
from torrent_edit import edit as edit_torrent

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

edit_torrent(torrents_list, tracker_list)