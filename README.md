# Getting Started With Python

## Hello, World!

If you're reading this, wecome! I assume you're from the audience of the "Beginner's Python" workshop, and it's good to have you here. You're probably used to the Google Collab/Jupyter environment, but this is a step forwards in both complexity, and eventual comfort. Consider this your first steps towards writing some serious Python code.

This repo is here to help you set up the software and tools you'll need to write anything from simple scripts to full-blown applications. By the end of this session you'll be able to run the included machine learning webapp, and hopefully feel comfortable making modifications to it yourselves.

![Welcome to your Python journey!](./static/baby-python.jpg "Python")

## What We Will Achive

Whenever you want to write code, there are normally a few steps in prepping your machine. We call this "preparing your toolchain", because we'll use multiple layers of tooling to make our lives writing code much, MUCH easier. This takes some time to get right, but I promise that it's worth it! Having your machine set up to run Python opens a world of opportunity for where you can go next.

Tonight's mission is to get all the required software for basic software development installed on your machine. We will start with some foundational tooling, and use it to install progressively more complicated tools. By the end, we'll be able to "clone" almost any open-source Python project and get it running.

### Why we're doing it

Once we have all of this done, we'll be able to play with an actual Python webapp that runs machine learning on your computer! We'll explain later what this webapp does, but in short it's an introduction to a framework called Streamlit. Streamlit is a very handy tool for using Python to write simple web-based GUI apps, and is the easiest way to make a user-friendly interface for all your Python projects. More on this down below

### Let me show you the way!

Some of the steps we'll go through might seem a little arbitrary - that's normal, and I hope you stick with me and trust that there are good reasons for each choice. In this document I'll explain a little bit about alternative choices where they exist, so you can try new toolchains in future.

The steps we'll explicitly cover in the setup phase are:

1. Installing VSCode
1. Installing Git and use it to pull this repo (hi guys!)
1. Basic command line usage
1. Installing Pyenv to make managing the Python language itself easy
1. Installing PDM to manage Python projects

### Installing VSCode

VSCode will be our "IDE" - integrated development environment. It's basically a text editor with a lot of handy features (like syntax highlighting, plugins) that make development a lot easier. One nice facet of VSCode is that we can use config files to automatically set up your development environment for you - great for workshops like this!

Follow the instructions below depending on your operating system.

#### Windows and MacOS

<details>
<summary></summary>

Go to the following link and down load the relevant 64-bit version:
https://code.visualstudio.com/download

</details>

#### Linux

<details>
<summary></summary>

```bash
sudo apt-get update && sudo apt-get install snapd
sudo snap install code
```

</details>

### Installing Git

Git is a kind of collaboration tool that allows us to easily share our code, and work with others on coding projects. At a high level, it lets me only "commit" the bits of a file that have changed to a remote "repository", which you can then `clone` or `pull`.

Git is an example of a "version control system". There are alternatives to Git, but in practice it's near universal in software engineering.

Follow the instructions below depending on your operating system.

#### Windows

<details>
<summary></summary>

1. Jump over here and downloadload the installer https://git-scm.com/download/win (64-bit Standalone)
1. Select `Use Visual Studio Code as Git's default editor` at the default editor screen
1. Select `Git from the command line and also from 3rd-party software` at the adjusting path environment screen

Most other options can just be clicked through

</details>

#### MacOS

<details>
<summary></summary>

```zsh
git --version
```

It will work if Git is already installed, otherwise it will prompt you to install. If xCode complains, then just do as it asks you to do.

</details>

#### Linux

<details>
<summary></summary>

```bash
sudo apt install git-all
```

</details>

### Basic command line usage

Open your command lines!

- Windows: run "Git Bash" from the Start menu
- Linux: `ctrl + alt + t`
- MacOS: `cmd + space`, then type in "terminal". Select the Terminal program

Moving around, doing folder stuff:

- `pwd` : Shows (prints) your current working directory/location in the folder structure
- `ls` : lists out the files in the current folder
  - `ls {path}` : Pass in a path (e.g. `ls ./static`) to see the files at that location
- `cd {path}` : Change directory to the target `{path}`
  - `~` = your home directory
  - `.` = your current directory
  - `..` = the directory above your current directory
  - `/` = the "root" of your file system
- `mkdir {dirname}` : creates a folder

Git commands:

- `git clone {url}` : pull down a new rsepo
- `git pull` : checks the remote server for newer versions of a git repo

VSCode commands:

- `code {path}` : opens VSCode with its "working directory" set to `{path}`

Let's create a new folder to hold all your coding projects, and move into it:

```bash
mkdir --parents ~/projects
cd ~/projects
git clone https://github.com/Oracen/python-intro.git
cd python-intro
ls .
```

Keep the terminal open for the next steps!

#### Linux and Mac Users Only:

<details>
<summary></summary>

Run the following command, and see what is named under the `CMD` heading:

```bash
ps -p $$
```

You should see either `bash` (a lot of Linux distros) or `zsh` (MacOS). If you see something else, you're probably a Linux geek and you know what you're doing. Inspect the shell-relevant scripts to see what envs we're setting.

</details>

### Installing PyEnv

From time to time, programming languages get an update. This makes a lot of people very angry and is been widely regarded as a bad move. (With apologies to Douglas Adams.)

Pyenv allows us to spend less time handling Python versions. A tool called Anaconda can also do this (as well as other things), but Anaconda comes with licencing conditions that make it unattractive for commercial work. It helps us recover if we accidentally break a Python install, it helps us upgrade, and it helps downstream tooling (such as VSCode or PDM) to switch Python versions based on availability.

Follow the instructions below based on your OS:

#### Windows

<details>
<summary></summary>

Installing Python is easy. Installing Python the right way (so that everything plays nice) is always a pain. Installing Pyenv is a pain, but it means making Python easy.

First, open PowerShell, and run the following command:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

Next, in Git Bash, run the following command:

```bash
. ~/projects/python-intro/bootstrap/bash-pyenv-profile.sh
```

(Don't forget the full-stop at the beginning!)

If this hasn't worked, uh...this workshop is about to get interesting!

</details>

#### Linux and MacOS

<details>
<summary></summary>

```bash
curl https://pyenv.run | $SHELL
```

Remember what shell you were using? If you're using `bash`, run the following:

```bash
. ~/projects/python-intro/bootstrap/bash-pyenv-profile.sh
```

If you're using `zsh`, run the following:

```zsh
. ~/projects/python-intro/bootstrap/zsh-pyenv-profile.sh
```

</details>

Now that Pyenv is installed, we can install Python easily:

```bash
pyenv install 3.10
pyenv global 3.10
```

Double check Python has been installed properly using `python --version`

### Installing PDM

Developing software can be hard for many reasons, but a major pain-point is differences in developer's machines causing bugs or outright failures. Package managers are a tool designed to simplify the process of replicating development environments. They do so by assisting with the search for installable code, resolving conflicts between versions, snapshotting the exact versions used by a developer, and bundling a lot of standardised scripting so e.g. my unit test command is the same as yours. They're quickly becoming a standard feature of modern programming languages.

Python didn't have a package manager for a long time, and the early attempts to make them have led to a very scattered build environment. Deploying Python apps used to be very painful! These days, there are a few choices for Python package managers. Still, we are living with the hangovers of the "old" Python build environment, and getting code working is sometimes still a challenge. This is particularly true in the AI/ML space.

We're going to be using PDM, as it "plays nicely" with almost everything in the Python ecosystem. Other common alternatives would be Anaconda and Poetry.

Install PDM with the following command:

```bash
curl -sSL https://pdm.fming.dev/install-pdm.py | python -
```

Test your install with `pdm --version`

## A Quick Intro to Streamlit

Right! If you're still with me, congrats! That seems like a whole lot of work, but I assure you it's worth it! We're now ready to see Streamlit!

Run `pdm start-demo` to begin!
