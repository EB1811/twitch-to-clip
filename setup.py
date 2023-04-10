from setuptools import setup, find_packages

setup(
    name="twitch-to-clip",
    description="Create vertical videos from twitch clips",
    version="0.5.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "twitch-to-clip = twitch_to_clip.__main__:main",
        ]
    },
)
