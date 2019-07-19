## Virtualenv

function set_virtualenv () {
  if test -z "$VIRTUAL_ENV" ; then
      PYTHON_VIRTUALENV=""
  else
      PYTHON_VIRTUALENV="${BLUE}[`basename \"$VIRTUAL_ENV\"`]${COLOR_NONE} "
  fi
}

function ps1command () {
    set_virtualenv
    export PS1="\n\e[1;96m\u@\h on \d at \@\n\e[1;92m$PYTHON_VIRTUALENV\w \$git_branch\[$txtred\]\$git_dirty\[$txtrst\] \e[0m\n\[\e[1;34m\]λ\[\e[m\] "
}

ps1command;
##

## Aliases
alias q=’exit’
alias c=’clear’
alias h=’history’
alias cs=’clear;ls’
alias p=’cat’
alias pd=’pwd’
alias lsa=’ls -a’
alias lsl=’ls -l’
alias pd=’pwd’
alias t=’time’
alias k='kill'
alias null=’/dev/null’
alias home='cd ~'
alias root='cd /'
alias open='xdg-open'
alias ..='cd ..'
alias ...='cd ..; cd ..'
alias ....='cd ..; cd ..; cd ..'
alias python='python3'
alias pip='pip3'
alias vimrc='vim ~/.vimrc'
alias bashrc='vim ~/.bash_profile'

export GREP_OPTIONS=' — color=auto'
export EDITOR=vim

