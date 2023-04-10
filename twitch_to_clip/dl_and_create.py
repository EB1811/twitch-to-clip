from twitch_to_clip.create_short import createShort
from twitch_to_clip.dl_twitch import downloadTwitch


def dlAndCreate(
    id: str, outputName: str = None, twitchdlArgs: list = None, ffmpegArgs: list = None
):
    print("\n---Downloading---\n")
    (title, user, game, outputVidName) = downloadTwitch(
        id, outputName=outputName, twitchdlArgs=twitchdlArgs
    )

    print("\n---Creating Video---\n")
    createShort(f"raw_{outputVidName}.mp4", f"{outputVidName}.mp4", ffmpegArgs)

    return (f"{outputVidName}.mp4", title, user, game)


def isVideo(url: str):
    return "/videos/" in url


def getIdFromUrl(url: str):
    if "/clip/" not in url and "/videos/" not in url:
        return url

    return (url.split("/videos/") if isVideo(url) else url.split("/clip/"))[1].split(
        "?"
    )[0]
