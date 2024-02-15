#shellcheck shell=sh

# Sublime over Vim where available
if [ -d "/Applications/Sublime Text.app" ]; then
  alias vim="subl --new-window"
  export EDITOR=subl_wait
fi
