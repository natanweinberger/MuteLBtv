''' Functions to manipulate Chromecast. '''
import pychromecast


def get_chromecast(chromecast_name):
    chromecasts, _ = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_name])

    if not chromecasts:
        raise Exception('Could not find Chromecast.')

    chromecast = chromecasts[0]
    chromecast.wait()

    return chromecast


def main(volume_status):
    chromecast = get_chromecast()
    chromecast.set_volume_muted(True if volume_status == 'true' else False)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
