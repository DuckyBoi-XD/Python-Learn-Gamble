from setuptools import setup, find_packages

setup(
    name="luckroom",
    version="0.1.0",
    description="A simple luck based game",
    author="Braedon Sy Tan",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "luckroom=LuckRoom:main"
        ]
    },
)