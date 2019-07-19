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
