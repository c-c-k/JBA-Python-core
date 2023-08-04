#!/usr/bin/env bash

set -o errexit

# test -d "$1"

# REPOSITORY_ROOT="$(cd $1; echo $PWD)"
REPOSITORY_ROOT="/dev/shm/memento"
REPOSITORY_SUBMODULES_FILE="/dev/shm/repos.txt"
# REPOSITORY_SUBMODULES_FILE="$REPOSITORY_ROOT/.gitmodules"
REPOSITORY_SUBMODULES_DIR="$REPOSITORY_ROOT/.git/modules"
TEMP_DIR="/dev/shm/tmpdir$(date +%s)"
SUB_COMMIT_MOD_FILE="$TEMP_DIR/pref"
SUB_COMMIT_PREFIX="unset" # set in sub_module_to_subtree
SUB_DIR_PREFIX="unset" # set in sub_module_to_subtree
SUB_PREFIX="unset" # set in sub_module_to_subtree
SUB_BASEDIR="unset" # set in sub_module_to_subtree
SUB_BASENAME="unset" # set in sub_module_to_subtree
SUB_GITDIR="unset" # set in sub_module_to_subtree
SUB_CLONE="unset" # set in sub_module_to_subtree

function init {
    echo "= starting submodules to subtrees conversion for: $REPOSITORY_ROOT ="
    cd "$REPOSITORY_ROOT"
    echo "== creating temp dir: $TEMP_DIR =="
    mkdir "$TEMP_DIR" || { echo "failed to create $TEMP_DIR"; exit; }
}

function fin {
    echo "== removing temp dir: $TEMP_DIR =="
    rm -fr "$TEMP_DIR"
}

function mod_repo_before_import {
    # while true
    # do
        echo "Repository for modification at:"
        echo "$SUB_CLONE"
        # echo 'enter "a" to abort or "c" to continue'
        select CHOICE_NAME in\
            "(m)odify repository in vim"\
            "(c)ontinue without modification"\
            "(a)bort conversion" 
        do
            case "$REPLY" in
                "m" )
                    cd "$SUB_CLONE"
                    read -p "enter prefix for commits in sub-repo: "
                    git --setup FILTER_BRANCH_SQUELCH_WARNING=1 filter-branch --msg-filter "echo -n '${REPLY}: ' && cat"
                    git branch --unset-upstream
                    git remote remove origin
                    # git rebase -i --root
                    vim +"-1tab Git log --oneline" +"vert Git rebase -i --root"
                    read -p "press anykey to continue"
                    return 0
                    ;;
                "c" )
                    return 0
                    ;;
                "a" )
                    fin
                    return 1
                    ;;
                * )
                    continue
                    ;;
            esac
        done
    # done
}

function sub_module_to_subtree {
    SUB_COMMIT_PREFIX="$1"
    SUB_DIR_PREFIX="$2"
    SUB_BASEDIR="$(dirname $SUB_DIR_PREFIX)"
    SUB_BASENAME="$(basename $SUB_DIR_PREFIX)"
    SUB_GITDIR="$REPOSITORY_SUBMODULES_DIR/$SUB_DIR_PREFIX"
    SUB_CLONE="$TEMP_DIR/$SUB_BASENAME"

    echo "== starting conversion of: $SUB_DIR_PREFIX =="
    # echo "=== copying $SUB_DIR_PREFIX to $TEMP_DIR ==="
    echo "=== cloning $SUB_DIR_PREFIX to $TEMP_DIR ==="
    # cp -r "$SUB_DIR_PREFIX" "$TEMP_DIR"
    git clone --no-local "$SUB_DIR_PREFIX" "$SUB_CLONE"
    # echo "=== stoping to allow for repository modification before subtree import ==="
    # mod_repo_before_import "$SUB_CLONE"
    echo "=== applying prefix to sub repo commits ==="
    echo "regex:(^.*$)==>${SUB_COMMIT_PREFIX}:\1" > "$SUB_COMMIT_MOD_FILE"
    cd "$SUB_CLONE"
    # echo "!!!!!"
    # echo "$SUB_COMMIT_MOD_FILE"
    # cat "$SUB_COMMIT_MOD_FILE"
    git filter-repo --replace-message "$SUB_COMMIT_MOD_FILE"
    # git log --oneline
    cd "$REPOSITORY_ROOT"
    # echo "debug: passed condition" && return
    echo "=== removing submodule $SUB_DIR_PREFIX ==="
    git rm "$SUB_DIR_PREFIX" && git commit -m "removed submodule $SUB_DIR_PREFIX"
    echo "=== creating subtree $SUB_DIR_PREFIX from $SUB_CLONE ==="
    git subtree --prefix "$SUB_DIR_PREFIX" add "$SUB_CLONE" master
    echo "=== removing $SUB_CLONE ==="
    rm -fr "$SUB_CLONE"
    rm -fr "$SUB_GITDIR"
}

init
# SUB_PREFIX_LIST=$(sed --silent -E "s/^\s+url = (.+)$/[ ] \1/p" "$REPOSITORY_SUBMODULES_FILE")
# echo "$SUB_PREFIX_LIST" | tee /dev/shm/repos_to_delete.md
# SUB_REPO_LIST=$(sed --silent -E "s/^\s+path = (.+)$/\1/p" "$REPOSITORY_SUBMODULES_FILE")
SUB_REPO_LIST="$(cat $REPOSITORY_SUBMODULES_FILE)"
for sub_repo in $SUB_REPO_LIST
# do sub_module_to_subtree "$sub_repo"
do sub_module_to_subtree $(echo $sub_repo|cut -d';' -f'1-' --output-delimiter=' ')
    # break
done
fin
