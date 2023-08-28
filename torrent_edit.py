from subprocess import run as runcommand


def edit(torrents_list, tracker_list):
    for torrent in torrents_list:
        for url in tracker_list:
            print(f'trying to edit {torrent}')
            runcommand([
                'transmission-edit',
                f'-a {url}',
                f'{torrent}',
                ])