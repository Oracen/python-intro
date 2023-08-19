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
1. (Optional) Set up Docker to make it easy to share your Python projects with others, so they don't have to set it all up!

### Installing VSCode

#### Windows and MacOS

Go to the following link and down load the relevant 64-bit version:
https://code.visualstudio.com/download

#### Linux

```bash
sudo apt-get update && sudo apt-get install snapd
sudo snap install code
```

### Installing Git

#### Windows

1. Jump over here and downloadload the installer https://git-scm.com/download/win (64-bit Standalone)
1. Select `Use Visual Studio Code as Git's default editor` at the default editor screen
1. Select `Git from the command line and also from 3rd-party software` at the adjusting path environment screen

Most other options can just be clicked through

#### MacOS

```zsh
git --version
```

It will work if Git is already installed, otherwise it will prompt you to install. If xCode complains, then just do as it asks you to do.

#### Linux

```bash
sudo apt install git-all
```

### Basic command line usage

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
git clone
cd python-intro
ls .
```

Keep the terminal open for the next steps!

### Installing PyEnv

#### Windows

Installing Python is easy. Installing Python the right way (so that everything plays nice) is always a pain. Installing Pyenv is a pain, but it means making Python easy.

First, open PowerShell, and run the following command:

## A Quick Intro to Streamlit

Right! If you're still with me, congrats! That seems like a whole lot of work, but I assure you it's worth it! We're now ready to see Streamlit!

Run `pdm start-demo` to begin!
