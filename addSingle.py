from torrent_edit import edit as edit_torrent
import re
from sys import argv
from shutil import copy as filecopy
from yaml import full_load as yamlload
from os import path as ospath


trackers_list_file = 'trackers.txt'
trackers_list = []
torrent_path = argv[1]
torrents_list = [torrent_path]

def config() -> dict:
    if ospath.exists('_config.yaml'):
        config_file = '_config.yaml'
    else:
        config_file = 'config.yaml'

    with open(config_file, 'r') as conffile:
        config_file = yamlload(conffile)
    return config_file

with open(trackers_list_file, 'r') as f:
    trackers = f.readlines()
    for urls in trackers:
            trackers_list.append(re.sub('\n', '', urls))

edit_torrent(torrents_list, trackers_list)

print(f'Copying {torrent_path} to {config()["upload_dir"]}')
filecopy(torrent_path, config()['upload_dir'])