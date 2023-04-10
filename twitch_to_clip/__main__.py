import argparse
from twitch_to_clip.dl_and_create import dlAndCreate, getIdFromUrl

parser = argparse.ArgumentParser()

# TODO customformated outputs
parser.add_argument('urls', nargs="+", type=str,
                    help='Twitch clip or highlight url/s')
parser.add_argument('-o', '--output', action='store', dest='output',
                    help='Output file name')
parser.add_argument('--twitchdl',
                    help='Arguments to pass to twitchdl download. Encase in quotes.')
parser.add_argument('--ffmpeg',
                    help='Optional ffmpeg command to apply to videos. Encase in quotes.')

# ! Script params
args = parser.parse_args()
urls = args.urls
output = args.output
twitchdlArgsString = args.twitchdl
ffmpegArgsString = args.ffmpeg


def main():
    print("urls:", urls)
    for url in urls:
        print("url:", url)
        # * Create videos from twitch
        (videoName, title, user, game) = dlAndCreate(
            getIdFromUrl(url), outputName=output,
            twitchdlArgs=convertToArgsArray(twitchdlArgsString),
            ffmpegArgs=convertToArgsArray(ffmpegArgsString)
        )

        print("Output Name:", videoName)

    print("---Done---")


def convertToArgsArray(args: str):
    return args.split(" ") if args else []
