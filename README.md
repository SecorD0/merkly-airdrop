<h1><p align="center">merkly-airdrop</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
  - [Windows](#Windows)
  - [Docker (image)](#Docker-image)
  - [Docker (building)](#Docker-building)
  - [Source code](#Source-code)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to:
- Parse eligible addresses.
- Find eligible addresses. 



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[merkly-airdrop](https://github.com/SecorD0/merkly-airdrop)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `addresses.db` — a temporary database.
  - `addresses.xlsx` — a spreadsheet for specifying addresses and viewing results.
  - `eligible_addresses.csv` — a file containing information about eligible addresses.
  - `errors.log` — a log file with errors that occurred during the work.
- `merkly-airdrop.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/merkly-airdrop/releases).
2. Create a folder and put the EXE file into it.
3. Run the program.
4. Enter `1` and press `Enter` to parse eligible addresses.
5. Insert addresses to be checked into the `addresses.xlsx` spreadsheet, save and close it.
6. Run the program again.
7. Enter `2` and press `Enter` to find eligible addresses. 
8. Open the `addresses.xlsx` spreadsheet and switch to the `Results` sheet to view the result of the program.
9. Delete the `files` directory.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program:
```sh
docker run -it --rm -v $HOME/merkly-airdrop/files:/program/files --name merkly-airdrop ghcr.io/secord0/merkly-airdrop:main
```
3. Enter `1` and press `Enter` to parse eligible addresses.
4. Insert addresses to be checked into the `addresses.xlsx` spreadsheet, save and close it.
5. Run the program again:
```sh
docker run -it --rm -v $HOME/merkly-airdrop/files:/program/files --name merkly-airdrop ghcr.io/secord0/merkly-airdrop:main
```
6. Enter `2` and press `Enter` to find eligible addresses. 
7. Open the `addresses.xlsx` spreadsheet and switch to the `Results` sheet to view the result of the program.
8. Delete the `files` directory.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/merkly-airdrop
```
3. Go to the repository:
```sh
cd merkly-airdrop
```
4. Build an image:
```sh
docker build -t merkly-airdrop .
```
5. Run the program:
```sh
docker run -it --rm -v $HOME/merkly-airdrop/:/program --name merkly-airdrop merkly-airdrop
```
6. Enter `1` and press `Enter` to parse eligible addresses.
7. Insert addresses to be checked into the `addresses.xlsx` spreadsheet, save and close it.
8. Run the program again:
```sh
docker run -it --rm -v $HOME/merkly-airdrop/:/program --name merkly-airdrop merkly-airdrop
```
9. Enter `2` and press `Enter` to find eligible addresses. 
10. Open the `addresses.xlsx` spreadsheet and switch to the `Results` sheet to view the result of the program.
11. Delete the `files` directory.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/merkly-airdrop
```
3. Go to the repository:
```sh
cd merkly-airdrop
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py`.
7. Enter `1` and press `Enter` to parse eligible addresses.
8. Insert addresses to be checked into the `addresses.xlsx` spreadsheet, save and close it.
9. Run the `app.py` again.
10. Enter `2` and press `Enter` to find eligible addresses. 
11. Open the `addresses.xlsx` spreadsheet and switch to the `Results` sheet to view the result of the program.
12. Delete the `files` directory.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn merkly-airdrop -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/merkly-airdrop/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop merkly-airdrop
```
2. Remove the container:
```sh
docker rm merkly-airdrop
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/merkly-airdrop:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop merkly-airdrop
```
2. Remove the container:
```sh
docker rm merkly-airdrop
```
3. Go to the repository:
```sh
cd merkly-airdrop
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t merkly-airdrop .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd merkly-airdrop
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/merkly-airdrop/files:/program/files --name merkly-airdrop ghcr.io/secord0/merkly-airdrop:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/merkly-airdrop/:/program --name merkly-airdrop merkly-airdrop
```

⠀To remove the container:
```sh
docker stop merkly-airdrop; docker rm merkly-airdrop
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/merkly-airdrop/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
