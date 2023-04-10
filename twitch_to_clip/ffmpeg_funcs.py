import os
import math
import subprocess
from subprocess import check_output


def createVerticalVideo(clipName: str, outputName: str):
    inputFile = f"raw_{clipName}"
    outputFile = f"{outputName}"

    command = f'ffmpeg -i "{inputFile}" -lavfi "[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256" -c:a copy "{outputFile}"'
    print("command", command)
    subprocess.run(command, shell=True)


def addBlackToEnd(clipName: str, outputName: str, time: str):
    inputFile = f"{clipName}"
    outputFile = f"{outputName}"

    command = f'ffmpeg -i "{inputFile}" -filter_complex "tpad=stop_duration={time}" "temp_{outputFile}"'
    print("command", command)
    subprocess.run(command, shell=True)

    os.replace(f"temp_{outputName}", f"{clipName}")


def getVidLength(clipName: str):
    inputFile = f"raw_{clipName}"

    command = (
        f'ffprobe -i "{inputFile}" -show_entries format=duration -v quiet -of csv="p=0"'
    )
    print("command", command)
    return math.floor(float(str(check_output(command, shell=True).decode("utf-8"))))


def customFinalCommand(clipName: str, command: str):
    """
    clipName: Name of the clip to be edited
    command: ffmpeg command e.g., "-af highpass=f=100 \"output.mp4\""
    """
    inputFile = f"{clipName}"

    command = f'ffmpeg -i "{inputFile}" {command}'
    subprocess.run(command, shell=True)
