import argparse
import sys
import pathlib

from .constants.information import APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION
from .utils.vision import ImageCoder

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
    '--height-shift',
    type=int,
    help='shift off height',
    default=1
)

parser.add_argument(
    '--width-shift',
    type=int,
    help='shift off width',
    default=1
)

parser.add_argument(
    "-s",
    "--show-size",
    action="store_true",
    help="show the ASCII image size as well",
)


def main() -> int:
    args = parser.parse_args()

    coder = ImageCoder(args.image)
    output = coder.serialize(args.width_shift, args.height_shift)

    if args.output:
        with open(args.output, 'w') as file:
            for line in output:
                file.write(''.join(line) + '\n')
            print(f'Saved file: {args.output}')
    else:
        for line in output:
            print(''.join(line))

    if args.show_size:
        coder.calculate_size()
        print(f'Image size: {coder.width}x{coder.height}')

    return 0


if __name__ == "__main__":
    sys.exit(main())
