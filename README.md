# Getting Started With Python

## Hello, World!

If you're reading this, welcome! I assume you're from the audience of the "Beginner's Python" workshop, and it's good to have you here. You're probably used to the Google Colab/Jupyter environment, but this is a step forwards in both complexity, and eventual comfort. Consider this your first steps towards writing some serious Python code.

This repo is here to help you set up the software and tools you'll need to write anything from simple scripts to full-blown applications. By the end of this session you'll be able to run the included machine learning webapp, and hopefully feel comfortable making modifications to it yourselves.

![Welcome to your Python journey!](./static/baby-python.jpg "Python")

## What We Will Achieve

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
sudo snap install code --classic
```

</details>

### Installing Git

Git is a kind of collaboration tool that allows us to easily share our code, and work with others on coding projects. At a high level, it lets me only "commit" the bits of a file that have changed to a remote "repository", which you can then `clone` or `pull`.

Git is an example of a "version control system". There are alternatives to Git, but in practice it's near universal in software engineering.

Follow the instructions below depending on your operating system.

#### Windows

<details>
<summary></summary>

1. Jump over here and download the installer https://git-scm.com/download/win (64-bit Standalone)
1. Select `Use Visual Studio Code as Git's default editor` at the default editor screen
1. Select `Git from the command line and also from 3rd-party software` at the adjusting path environment screen

Most other options can just be clicked through

</details>

#### MacOS

<details>
<summary></summary>

First, enable developer tools with the following command:

```zsh
xcode-select --install
```

To make later steps a little easier, we're going to install a package manager called Homebrew. This is fairly simple, if you run the following command.

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then use the following to activate the `brew` command:

```zsh
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Check the install with `brew --version`. If the installer asks you to do anything, just select the default options. You can also disable the analytics with the following command:

```zsh
brew analytics off
```

Finally, try to check Git:

```zsh
git --version
```

It will work if Git is already installed, otherwise it will prompt you to install. If XCode complains, then just do as it asks you to do.

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

- `git clone {url}` : pull down a new repo
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

Pyenv allows us to spend less time handling Python versions. A tool called Anaconda can also do this (as well as other things), but Anaconda comes with licencing conditions that make it unattractive for commercial work. Pyenv helps us recover if we accidentally break a Python install, it helps us upgrade, and it helps downstream tooling (such as VSCode or PDM) to switch Python versions based on availability.

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
. ~/projects/python-intro/bootstrap/bash-pyenv-win-profile.sh
```

(Don't forget the full-stop at the beginning!)

If this hasn't worked, uh...this workshop is about to get interesting!

</details>

#### MacOS

<details>
<summary></summary>

Pyenv installation is fairly simple on MacOS, as Homebrew will do a lot of the heavy lifting here:

```zsh
brew install openssl readline sqlite3 xz zlib tcl-tk
brew install pyenv
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

#### Linux

<details>
<summary></summary>

Python build has quite a few requirements to compile, so install them first then install PyEnv

```bash
sudo apt-get install make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
        libffi-dev liblzma-dev
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
pyenv install 3.10.11
pyenv global 3.10.11
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

Normally you'd need to "put the tool on the path" by adding a line to your shell's config, but I sneakily did that in the PyEnv setup for you :P

Test your install with `pdm --version`

If it works, go ahead and install this repo with the following command:

```bash
pdm install
```

## A Quick Intro to Streamlit

Right! If you're still with me, congrats! That seems like a whole lot of work, but I assure you it's worth it! We're now ready to see Streamlit!

Run `pdm start-demo` to begin!

### What is Streamlit?

Streamlit lets us write simple web applications without having to learn web code (Javascript, HTML and CSS). It's great for data science workflows as we can write the application code in the same language as our data analyses are written in. Streamlit is a handy tool to write quick tools to help coworkers and to show to stakeholders or clients as a PoC.

With a bit of extra effort, it's actually possible to make full production-ready data apps in Streamlit, using techniques like caching to improve performance. However, if you're building a data app, remember to learn a bit about security before getting too carried away!

Before we begin, let's quickly talk a little about how websites work. The "default" way to show a website on the internet is to provide a HTML file (plus other bits) on a computer somewhere. You then run a "webserver" on that machine, which can listen to HTTP requests and allow remote users to download the files to their browser. The browser then shows the content to the user. If you want to see this in action, open a new window, hit `F12` (in Chrome) and refresh the page. By looking at the `Network` and `Sources` tab you can see all the pages loading.

### How Streamlit Works

At it's core, Streamlit has 3 core components that we need to be aware of:

1. A webserver
1. A framework for webapp generation
1. A way of working that's very familiar to data developers

#### Webserver

Streamlit provides you with a handy little webserver to serve the code to your own machine. It's not built for production workloads but it does have some advantages - namely, it runs Python code (as opposed to static files) and has a debugger that understands the unique blend of scripting that Streamlit uses. This is what we are using to show the Streamlit app in your browser.

#### Webapp Generation Framework

But browsers understand HTML, not Python, right? Well, Streamlit interprets for us, from Python to our web languages. Streamlit is kind of like templates for web code, where chunks of dynamic data is combined with static templates to make a full webpage. This may sound strange, but is very similar to the way modern web frameworks like React or Vue work. Basically, your browser thinks it's talking to a webserver sending a standard web file, with updates being patched in as they are available. But your webserver is secretly turning Python into HTML files and javascript scripts, and sending them over as they're ready.

Unlike React or Vue, the majority of your logic ISN'T written in Javascript. This means the web document you generate can't be as dynamic ("reactive") as a full app written in Node or pure JS/HTML. While JS code can dynamically update almost any part of the screen, the HTML code generated by Streamlit is way chunkier and more rigid/less flexible. Streamlit also doesn't know which parts of the app need to be updated in response to user input, meaning the whole application needs to be "recalculated" in response to changes.

#### Application Model

This isn't the end of the world though! Avoiding remembering "state" is a really clever design decision when it comes to keeping systems simple, because "idempotence" means we're less likely to get weird bugs caused by failing to reset elements on refresh. As a Python dev, we simply decide what we want to appear on the screen, and writing them into the script in the order which we want to show them. The script ends up looking like the web page, with "titles" up top and content being calculated in similar places where it's displayed. This "script-based" approach is very natural to Python devs, so you should feel right at home with Streamlit if you've ever written a utility script in Python.

Sometimes you'll want things to behave more like a web app though. Maybe you need to calculate a value at the bottom of a script but display it up the top of the app page. Maybe you want to remember the results of some slow calculations. Streamlit gives you the tools to make these decisions, but never makes these choices for you. This way you only need to add complexity to your app if you decide that it's important (e.g. to improve performance).

## Enough Theory!

Let's get onto practice!

Feel free to follow along with the interactive demo, or tinker around with Streamlit yourself. If you want to do a bit of solo exploration, you might find the docs helpful as a source of copy-pa...uh, I mean, examples!

https://docs.streamlit.io/library/api-reference

The base Streamlit library is nice, but it is far from complete. Often you'll find yourself needing extra bits to make your app "pop". For example, you may want to include [a Streamlit implementation of the popular Folium library](https://folium.streamlit.app/) (yes, that site is a streamlit app) for a geospatial project you're working on. You can use PDM to make sure that requirement is included with your code using the command

```bash
pdm add streamlit-folium
```

By adding the library this way (as opposed to `pip install`) you can be sure that others will be able to get your code working on their machines, all without the bugs and issues coming from loose version management.
