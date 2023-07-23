#!/bin/bash

# This script copies files that are common between Scheherazade, Harmattan, and 
# Lateef font projects repo to the related project repos.

# Copyright (c) 2023 SIL International  (https://www.sil.org)
# Released under the MIT License (http://opensource.org/licenses/MIT)

# Requires:
#   Related project repo clones are all siblings in the file tree.
#   Current working directory is the root folder of one of the related project repo clones

set -e

# Allow a -v to enable more verbose output

verbose=
while getopts 'vh' opt; do
  case "$opt" in
    v)
      verbose=' -v '
      ;;

    ?|h)
      echo "Usage: $(basename $0) [-v]"
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"

# Relative path to all repo clones of related projects:

repos=(
    ../font-harmattan
    ../font-lateef
    ../font-scheherazade
    ../font-arab-tools
)

# Files to be copied:

# Caution: do not use wildcards unless you are very sure that the 
#    list of matching files is the same for every every repo!
files=(
    tools/abscopySHLfiles.sh
    tools/absgenftml.py
    tools/absgenclasses.py
    source/opentype/gsub.feax
)

# Make sure current working directory is the root one of the above repos
me=$(basename `pwd`)
if [[ ! " ${repos[@]} " =~ " ../$me " ]]; then
    echo "Please cd to root of the repo to use" $(basename "$0")
    echo "then use ./tools/nameofscript.sh"
    exit 2  
fi

# Iterate through repos, using each one (other than myself) as a destination
for repo in "${repos[@]}"
do
    if [[ "$repo" != "../$me" ]]; then
        # Iterate through repos and make sure none are behind their default remote.
        # If any are behind, then exit with a warning.
        cd $repo
        git fetch -q
        CURRENTBRANCH=$(git rev-parse --abbrev-ref HEAD)
        HEADHASH=$(git rev-parse HEAD)
        UPSTREAMHASH=$(git rev-parse $CURRENTBRANCH@{upstream})
        if [ "$HEADHASH" != "$UPSTREAMHASH" ] ; then
           git status -s -b --show-stash --ahead-behind --renames
           echo "$repo: $CURRENTBRANCH not up to date with origin/$CURRENTBRANCH. Stopping."
           echo "Please update the local repository by doing a git pull"
           exit 0
        else
           # Copy files from me to another repo
           echo -e "\nSending files from $me to $repo"
           for file in "${files[@]}"
                do
                    if cmp -s "$file" "$repo/$file" ; then
                        # Target copy is already up-to-date; output msg if in verbose mode
                        [[ ! -z "$verbose" ]] && echo " already up to date: $repo/$file"
                    else
                    # Target file needs updating
                    # Would use the simpler cp --parents here but not supported on macOS
                    mkdir -p `dirname "$repo/$file"` &&  cp $verbose -p "$file" "$_"
                    fi
                done
        fi
    echo " Done"
    fi
done
