import shutil
from twitchdl import twitch, console
from twitchdl.commands import download
import string

parser = console.get_parser()


def downloadTwitch(
    tId: str, outputName: str = None, twitchdlArgs: list = None, video: bool = False
):
    """
    Downloads a twitch clip or video and returns the title, user, game, and output name.
    @tId: The id of the twitch clip or video.
    @outputName: The name of the output file.
    @twitchdlArgs: A list of arguments to pass to twitchdl, in argparse list form.
    @video: Whether the id is for a video or not.
    """

    vidInfo = twitch.get_clip(tId) if not video else twitch.get_video(tId)
    if not vidInfo:
        print("No video info")
        return

    if vidInfo["durationSeconds"] > 600:
        print("Video too long")
        return

    title = vidInfo["title"]
    user = vidInfo["broadcaster"]["login"] if not video else vidInfo["creator"]["login"]
    game = vidInfo["game"]["name"]

    # Need to remove punctuation from title for ffmpeg
    outputVidName = (
        title.translate(str.maketrans("", "", string.punctuation))
        if not outputName
        else outputName
    )

    args = parser.parse_args(
        ["download"]
        + [tId]
        + removeArgs(twitchdlArgs[:], ["-f", "--format", "-o", "--output"])
        + ["-f", "mp4"]
        + ["-o", "temp.{format}"]
        + (
            ["-q", "source"]
            if not any(flag in twitchdlArgs for flag in ["-q", "--quality"])
            else []
        )
    )
    print(args)
    download(args)
    shutil.move(f"temp.mp4", f"raw_{outputVidName}.mp4")

    return (title, user, game, outputVidName)


def removeArgs(args: list, argsToRemove: list):
    for arg in argsToRemove:
        if arg in args:
            index = args.index(arg)
            del args[index : index + 2]

    return args


# flags = ' '.join(f'{key} {value}' for key, value in flags.items() if value)
# downloadCommand = f"twitch-dl download {tId} {flags}"
# subprocess.call(downloadCommand)
