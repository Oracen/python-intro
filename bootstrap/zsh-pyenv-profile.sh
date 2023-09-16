echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.zshrc

echo "Shell environment set up, exit to force restart"