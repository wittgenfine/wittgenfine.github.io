#!/bin/bash 


git filter-branch --commit-filter
'if [ "$GIT_AUTHOR_EMAIL" = "parkerhagmaier@gmail.com" ]'; then 
  skip_commit "$@";
else 
  git commit-tree "$@";
fi' -- -- all

