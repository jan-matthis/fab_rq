import sys
from pathlib import Path

from fabric.main import program


def main():
    sys.argv = ['fab', '-r', str(Path(__file__).parent), '-F', 'nested', '--echo'] + sys.argv[1:]
    if len(sys.argv) == 6:
        sys.argv += ['--list']
    program.run()


def main_debug():
    sys.excepthook = pdb_hook
    main()


def pdb_hook(type, value, tb):
    if hasattr(sys, "ps1") or not sys.stderr.isatty():
        sys.__excepthook__(type, value, tb)
    else:
        import traceback

        try:
            import ipdb as pdb

        except:
            import pdb

        traceback.print_exception(type, value, tb)
        pdb.post_mortem(tb)


if __name__ == '__main__':
    main()
