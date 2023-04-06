import argparse
import sys
import pathlib

from acsii.constants.information import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION
from acsii.utils.vision import Encoder

parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    '-i',
    '--image',
    type=pathlib.Path,
    help='path to image file',
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    help='output (text) file',
)

parser.add_argument(
    "-s",
    "--show-size",
    action="store_true",
    help="show the ASCII image size as well",
)

parser.add_argument(
    "-t",
    "--typeset",
    type=str,
    choices=['nums', 'alphs', 'syms'],
    default='syms',
    help="ASCII characters type",
)


def main() -> int:
    args = parser.parse_args()

    encoder = Encoder(args.image, args.typeset)
    output = encoder.serialize()

    if args.output:
        with open(args.output, 'w') as file:
            for line in output:
                file.write(''.join(line) + '\n')
            print(f'Saved file: {args.output}')
    else:
        for line in output:
            print(''.join(line))

    if args.show_size:
        encoder.calculate_size()
        print(f'Image size: {encoder.width}x{encoder.height}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
