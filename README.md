Twitch-To-Clip
=================

CLI tool that allows you to download Twitch clips or highlight videos and convert them into vertical videos ideal for TikTok and YouTube shorts.
It uses the [twitch-dl](https://github.com/ihabunek/twitch-dl ) and ffmpeg packages to achieve this.




Requirements
---------
- Python 3.7 or higher installed on your system
- [ffmpeg](https://ffmpeg.org/download.html), installed and on the system path

To check if ffmpeg is properly installed on your system, open your terminal and run the following command:
```shell
ffmpeg -version
```
If ffmpeg is installed and added to the system path, it will display the version information.

Usage
---------

To use the package, run the twitch-to-clip command followed by the Twitch clip or highlight URL/s you want to download and convert into vertical video.

```shell
twitch-to-clip "twitch clip or highlight URL/s"
```

Supports the following custom arguments:

- --output (-o) : Specify the output file name
- --twitchdl : Add additional arguments to the twitch-dl download command. Encase in quotes.
- --ffmpeg : Optional ffmpeg command to apply to videos. Encase in quotes.

```shell
Usage: twitch-to-clip [-h] [--output OUTPUT] [--twitchdl TWITCHDL]
                      [--ffmpeg FFMPEG]
                      urls [urls ...]

Create vertical videos from twitch clips

positional arguments:
  urls                  Twitch clip or highlight url/s

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file name
  --twitchdl TWITCHDL   Arguments to pass to twitchdl download. Encase in
                        quotes.
  --ffmpeg FFMPEG       Optional ffmpeg command to apply to videos. Encase in
                        quotes.
```


Example
---------
To download and convert a Twitch clip to a vertical video, run the following command:

```shell
twitch-to-clip "https://www.twitch.tv/jerma985/clip/ScaryLittleKleePoooound-chk_kaV2M2xZuzV5"
```

You can also specify the output file name using the --output (-o) argument:

```shell
twitch-to-clip "https://www.twitch.tv/jerma985/clip/ScaryLittleKleePoooound-chk_kaV2M2xZuzV5" -o myclip.mp4
```

If you want to add additional arguments that can be passed throught to the twitch-dl download command or apply an optional ffmpeg command to the downloaded video, you can use the --twitchdl and --ffmpeg arguments respectively.

```shell
twitch-to-clip "https://www.twitch.tv/jerma985/clip/ScaryLittleKleePoooound-chk_kaV2M2xZuzV5" --twitchdl "-q 720p" --ffmpeg "-af highpass=f=100 \"output.mp4\""
```

Useful Links
-------
https://twitch-dl.bezdomni.net/

https://ffmpeg.org/

Author
-------
This package was created by Emmanuil B.

License
-------
Copyright 2023 Emmanuil Borovikovs <https://eb1811.github.io/>

Licensed under the GPLv3: http://www.gnu.org/licenses/gpl-3.0.html