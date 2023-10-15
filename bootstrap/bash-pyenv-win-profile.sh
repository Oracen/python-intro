echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

echo 'export PATH=$HOME/AppData/Roaming/Python/Scripts:$PATH' >> ~/.bash_profile
echo 'export PATH=$HOME/AppData/Roaming/Python/Scripts:$PATH' >> ~/.bashrc

echo "Shell environment set up, exit to force restart"