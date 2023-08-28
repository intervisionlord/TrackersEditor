from torrent_edit import edit as edit_torrent
import re
# import os
# from sys import argv
import torrent_edit
from shutil import copy as filecopy
from yaml import full_load as yamlload

trackers_file = 'trackers.txt'
# torrents_dir = argv[1]
tracker_list = []
torrent_path = input('Enter a full path to single torrent: ')
torrents_list = [torrent_path]

with open('_config.yaml', 'r') as conffile:
    config = yamlload(conffile)

with open(trackers_file, 'r') as f:
    trackers = f.readlines()
    for urls in trackers:
        tracker_list.append(re.sub('\n', '', urls))

edit_torrent(tracker_list, torrents_list)

filecopy(torrent_path, config['upload_dir'])