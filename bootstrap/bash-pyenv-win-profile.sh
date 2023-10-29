echo 'export PYENV_ROOT="$HOME/.pyenv/pyenv-win"' >> ~/.bashrc
echo 'export PYENV=$PYENV_ROOT' >> ~/.bashrc
echo 'export PYENV_HOME=$PYENV_ROOT' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv/pyenv-win"' >> ~/.bash_profile
echo 'export PYENV=$PYENV_ROOT' >> ~/.bash_profile
echo 'export PYENV_HOME=$PYENV_ROOT' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"' >> ~/.bash_profile

echo 'export PATH=$HOME/AppData/Roaming/Python/Scripts:$PATH' >> ~/.bash_profile
echo 'export PATH=$HOME/AppData/Roaming/Python/Scripts:$PATH' >> ~/.bashrc

echo "Shell environment set up, exit to force restart"
