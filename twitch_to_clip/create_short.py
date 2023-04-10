from twitch_to_clip.ffmpeg_funcs import createVerticalVideo, addBlackToEnd, getVidLength


# * Example
# createYtShort("raw_video.mp4", "video.mp4", [
#     lambda name, out, file: audioFilter(name, out, file, "highpass=f=90")
# ])
def createShort(clipName: str, outputName: str, ffmpegArgs: list = []):
    createVerticalVideo(clipName, outputName)

    videoLength = getVidLength(outputName)
    if videoLength < 15:
        addBlackToEnd(outputName, outputName, 15 - videoLength)

    # for func in ffmpegFuncs:
    #     func(outputName, outputName)
