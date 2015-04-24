__version__ = '0.0'


def get_version(cmd_ver):
    return '%(prog)s: v{0}, saio-tools: v{1}'.format(
        cmd_ver, __version__)
