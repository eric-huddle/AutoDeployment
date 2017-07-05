#!/bin/bash

echo -n "Which branch do you want to pull > "
read branch
if [ ! $branch ]; then
  echo "Branch name should not be NULL."
  exit 1
else
  git checkout $branch
  if [ $? != 0 ]
  then
    echo "Please make sure the name of the branch exists."
    exit 1
  else
    git fetch
    git diff --name-only $branch remotes/origin/$branch | tee git_diff_result.txt
    echo -n "Do you want to deploy the code[Y/N]:"
    read choice
    case $choice in
    N|n|no|No)
      exit 1
    ;;
    Y|y|yes|Yes)
# start deploy the code
      git pull
      if [[ $(grep "requirements.txt" git_diff_result.txt) ]]
      then
        echo "requirements.txt has been modified"
        pip install -r requirements.txt
        sed -i '/requirements.txt/d' git_diff_result.txt
      fi
      
      if [[ $(grep "package.json" git_diff_result.txt) ]]
      then
        echo "packages.json has been modified"
        npm install
        sed -i '/package.json/d' git_diff_result.txt
      fi
      
      if [[ $(grep "bower.json" git_diff_result.txt) ]]
      then
        echo "bower.json has been modified"
        bower install
        sed -i '/bower.json/d' git_diff_result.txt
      fi
      
      if [[ $(grep "/migrations/" git_diff_result.txt) ]]
      then
        echo "migrations has been modified"
        ./manage.py migrate
      fi
      
      if [[ $(grep "frontend" git_diff_result.txt) ]] || [[  $(grep "backend/settings" git_diff_result.txt) ]]
      then
        echo "frontend or backend/settings has been modified"
        gulp build
        sed -i '/frontend/d' git_diff_result.txt
        sed -i '/backend\/setting/d' git_diff_result.txt
      fi
      
      if [[ $(grep "backend" git_diff_result.txt) ]]
      then
        echo "backend has been modified"
        find . -name '*.pyc' | xargs rm
        sed -i '/backend/d' git_diff_result.txt
      fi
      
      if [[ -s git_diff_result.txt ]]
      then
        echo "There is something wrong with the code updating. Please check git_diff_result.txt"
      else
        echo "Congratulation! Code update finished!"
      fi
    ;;
    *)
      echo "Illegal input. Please input Y/N." 
      exit 1
    esac
  fi
fi


