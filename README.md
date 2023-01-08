# Sublime Text & Merge Configurations

What's nicer that having all your configurations version controlled and synced between your work and personal machines?

I use [HomeSchick](https://github.com/andsens/homeshick) to manage my configs. So they are formatted to be checked out and linked by me.

## Folders of Note

The `Users` folder is my Sublime Text ~~4~~ Users Package
The `Users-Sublime-Merge` is unsurprisingly my Sublime Merge Users Package
The `home/bin` has my shell scripts I use to enhance both

## Sublime Merge and GitHub/GitLab/Bitbucket Integration

I use an amazing git alias found on [the Sublime Merge Discourse Forum](https://forum.sublimetext.com/t/github-gitlab-bitbucket-integration-commands-menu-items/53893).

In case that post vanishes here is the git alias for 'open'

```shell
git config --global alias.open '!f() {
    local type="${1:-branch}"
    local target="${2:-HEAD}"
    local remote="origin"

    if [ "$type" = "branch" -o "$type" = "pr" ]; then
        # get full name (i.e. refs/heads/*; refs/remotes/*/*); src: https://stackoverflow.com/a/9753364
        target="$(git rev-parse --symbolic-full-name "$target")"

        if [ "$target" != "${target#"refs/remotes/"}" ]; then
            # extract from remote branch reference
            target="${target#"refs/remotes/"}"
        else
            # extract from local branch reference; src: https://stackoverflow.com/a/9753364
            target="$(git for-each-ref --format="%(upstream:short)" "$target")"
        fi
        # split remote/branch
        remote="${target%%/*}"
        target="${target#"$remote/"}"

        if [ -z "$remote" ]; then
            echo "Branch ($2) does not point to a remote repository." >&2
            return 2
        fi
    fi

    local repo_url="$(git remote get-url "$remote" | sed -E -e "s/(\.(com|org|io))\:/\1\//" -e "s/git@/https:\/\//" -e "s/\.git$//")"
    if [ -z "$repo_url" ]; then
        echo "Cannot open: no remote repository configured under (origin)" >&2
        return 1
    fi

    case "$(tr "[:upper:]" "[:lower:]" <<< "$repo_url")" in
        *github*)
            [ "$type" = "commit" ] && repo_url="$repo_url/commit/$(git rev-parse "$target")"
            [ "$type" = "pr"     ] && repo_url="$repo_url/compare/$target?expand=1"
            [ "$type" = "tag"    ] && repo_url="$repo_url/releases/tag/$target"
            [ "$type" = "branch" ] && repo_url="$repo_url/tree/$target"
            ;;
        *bitbucket*)
            [ "$type" = "commit" ] && repo_url="$repo_url/commits/$(git rev-parse "$target")"
            [ "$type" = "pr"     ] && repo_url="$repo_url/pull-requests/new?source=$target"
            [ "$type" = "tag"    ] && repo_url="$repo_url/src/$target"
            [ "$type" = "branch" ] && repo_url="$repo_url/src/$target"
            ;;
        *gitlab*)
            [ "$type" = "commit" ] && repo_url="$repo_url/-/commit/$(git rev-parse "$target")"
            [ "$type" = "pr"     ] && repo_url="$repo_url/-/merge_requests/new?merge_request[source_branch]=$target"
            [ "$type" = "tag"    ] && repo_url="$repo_url/-/tags/$target"
            [ "$type" = "branch" ] && repo_url="$repo_url/-/tree/$target"
            ;;
        *)
            echo "Cannot open: not a GitHub, GitLab, or Bitbucket repository" >&2
            return 1
            ;;
    esac

    open "$repo_url"
}; f'
```
