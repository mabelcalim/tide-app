#!/bin/sh
PATH="~/bin:/sbin:/bin:/var/sbin:/var/bin:/usr/local/bin:$PATH"
cd /Users/usuario/git_repos/tide-app/
git pull
git add -A .
git commit -q -m 'automated update'
git push -q

Run

  git config  user.email "mabelcalim@gmail.com"
  git config  user.name "mabelcalim"
  git config  user.password "21ma04bel84"
~                                       
