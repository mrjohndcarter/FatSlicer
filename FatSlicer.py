import argparse
import subprocess

from os.path import isfile


def get_architectures(path):
    output = subprocess.check_output(['lipo', '-info', path])
    archs = output.split()
    return archs[archs.index('are:') + 1:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('libname', help='name of the fat file to split', type=str)
    args = parser.parse_args()

    if not isfile(args.libname):
        print 'could not find library: %s' % args.libname
        return

    assert isinstance(args.libname, str)
    archs = get_architectures(args.libname)

    for arch in archs:
        subprocess.check_call(["lipo", args.libname, "-thin", arch, "-output", "".join([args.libname, ".", arch])])


if __name__ == '__main__':
    main()
