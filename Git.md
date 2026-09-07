## Key Git Concepts

- **Repository:** A folder where Git tracks your project and its history.
- **Clone:** Make a copy of a remote repository on your computer.
- **Stage:** Tell Git which changes you want to save next.
- **Commit:** Save a snapshot of your staged changes.
- **Branch:** Work on different versions or features at the same time.
- **Merge:** Combine changes from different branches.
- **Pull:** Get the latest changes from a remote repository.
- **Push:** Send your changes to a remote repository.

## Git Configure
``` shell
git config --global user.name "Your Name"
git config --global user.email "Email@example.com"
```
- **System** (all users): `git config --system`
- **Global** (current user): `git config --global`
- **Local** (current repo): `git config --local`
ordered ascendingly 


``` shell
git config --list
git config user.name
```
you could write the specific setting to see its value like user.name above


to remove a setting you could use ```--unset``` 
``` shell 
git config --global --unset
```

set a default name for the branch:
```shell
git config --global init.defaultBranch main
```

## Git Commands

``` shell
git init
```
makes a .git files that starts working in the folder

### Staging Commands
- `git add <file>` - Stage a file
- `git add --all` or `git add -A` - Stage all changes
- `git status` - See what is staged
- `git restore --staged <file>` - Unstage a file
### Committing Commands
Here are some key commands for commits:
- `git commit -m "message"` - Commit staged changes with a message
- `git commit -a -m "message"` - Commit all tracked changes (skip staging)
- `git log` - See commit history
- `git log --oneline` For a shorter view
- `git log --stat` To see which files changed in each commit
If you just type `git commit` (no `-m`), your default editor will open so you can write a detailed, multi-line message
- **Create an empty commit:**  
    `git commit --allow-empty -m "Start project"`
- **Use previous commit message (no editor):**  
    `git commit --no-edit`
- **Quickly add staged changes to last commit, keep message:**  
    `git commit --amend --no-edit`
 - **Accidentally committed the wrong files?**  
	You can use `git reset --soft HEAD~1` to undo the last commit and keep your changes staged.

``` shell
git push
```
pushes the committed changes to the host (platform like GitHub, GitLab, or etc.)

### Tagging
We use tagging as a bookmark for a special commit or something:
- `git tag <tagname>` - Create a lightweight tag
- `git tag -a <tagname> -m "message"` - Create an annotated tag
- `git tag <tagname> <commit-hash>` - Tag a specific commit
- `git tag` - List tags
- `git show <tagname>` - Show tag details

- **Annotated Tag:** Stores author, date, and message. Recommended for releases and sharing with others.
- **Lightweight Tag:** Just a simple name for a commit (no extra info, like a bookmark).

tags are local, you can push them using:
```shell
git push origin v1.0 
git push --tags
```
know that you have to specify, pushing only will not tags
to delete them:
```shell
git tag -d v1.0
git origin push --delete tag v1.0
```
to replace or change a tag:
```shell
git push --force origin v1.0 
git tag -f v1.0 <commit hash>
```

### Stashing
- `git stash` - Stash your changes
- `git stash push -m "message"` - Stash with a message
- `git stash list` - List all stashes
- `git stash show` - Shows changes
- `git stash show -p` - Shows detailed changes
- `git stash apply` - Applies the latest stash from the stack (without popping it)
- `git stash apply stash@{i}` - Apply stash i from the stack
- `git stahs pop` - Apply the latest stash and remove it from the stack
- `git stash drop` - Remove the stash stash@{i} from the stack
- `git stash clear` - Remove all stashes
- `git stash branch <branchname>` - Create a branch from a stash
to stash is to keep the edited but not ready yet version of the code and get the last committed one to do something, you could merge them later of course

to stash untracked files too, use `git stash -u` (or `--include-untracked`)
and stashes are sorted as a stack

### History
- `git log` - Show full commit history
- `git log --oneline` - Show a summary of commits
- `git log author="eyad"` - Show the commit history made by that user
- `git log since="2 weeks ago"` - Show commit history up until two weeks ago
- `git log --stat` - Show files changed per commit
- `git log --graph` - Show graph of branch history
- `git show <commit>` - Show details of a specific commit
- `git diff` - See unstaged changes between yours and the last commit
- `git diff --staged` - See staged changes between you last commit
you could use / to search for a word, press n for the next match and q to quit
you could use `git diff hash1 hash2` to compare two commits

### Help
- `git help <command>` - See the manual page for a command
- `git <command> --help` - See help for a command (same as above)
- `git <command> -h` - See a quick summary of options
- `git help --all` - List all possible Git commands
- `git help -g` - List guides and concepts

- Use the **arrow keys** or `Space` to scroll down, `b` to scroll up.
- Type `/` followed by a word to search (e.g., `/option`), then `n` for next match.
- Press `q` at any time to quit the help view.
- `SHIFT + G` to jump the end of the list

# https://www.w3schools.com/git/git_branch.asp?remote=github