from twitch_to_clip.ffmpeg_funcs import (
    createVerticalVideo,
    addBlackToEnd,
    getVidLength,
    customFinalCommand,
)


def createShort(clipName: str, outputName: str, ffmpegArgs: str = None):
    createVerticalVideo(clipName, outputName)

    # videoLength = getVidLength(outputName)
    # if videoLength < 15:
    #     addBlackToEnd(outputName, outputName, 15 - videoLength)

    if ffmpegArgs:
        print("\n---applying custom ffmpeg arguments---\n")
        customFinalCommand(outputName, ffmpegArgs)
