from torrent_edit import edit as edit_torrent
import re
from sys import argv
from shutil import copy as filecopy
from yaml import full_load as yamlload

# torrent_file = argv[1]
# torrent_path = input('Enter a full path to single torrent: ')
trackers_list_file = 'trackers.txt'
trackers_list = []
torrent_path = argv[1]
torrents_list = [torrent_path]

with open('_config.yaml', 'r') as conffile:
    config = yamlload(conffile)

with open(trackers_list_file, 'r') as f:
    trackers = f.readlines()
    for urls in trackers:
        trackers_list.append(re.sub('\n', '', urls))

edit_torrent(torrents_list, trackers_list)

print(f'Copying {torrent_path} to {config["upload_dir"]}')
filecopy(torrent_path, config['upload_dir'])