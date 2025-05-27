# GIT CHEAT SHEET
Key concepts

---

## Setup / Basics
- `git --version`
- `git config --global user.name "Your Name"`
- `git config --global user.email "you@example.com"`
- `git config --global init.defaultBranch main` – Set default branch
- `git config --list` – View config
- `git log <file>` – View a specific files history

---

## Repositories
- `git init` – Start a new repo
- `git status` – Check repo status
- `git add <file>` – Stage changes
- `git add .` – Stage all changes
- `git stash` – Stash changes
- `git commit -m "message"` – Commit changes
- `git commit --amend` – Amend last commit 
- `.git/` – Hidden directory storing repo data

---

## Internals
- Git stores data as **snapshots**, not diffs
- Commits point to trees/blobs
- `HEAD` – Points to current branch
- `git log` – Show commit history
- Hashes (SHA-1) uniquely identify commits

---

## Config
- Global vs Local config
  - Global: `~/.gitconfig`
  - Local: `.git/config`
- Aliases:  
  `git config --global alias.co checkout`

---

## Branching
- `git branch` – List branches  
- `git branch <name>` – Create branch  
- `git checkout <branch>` – Switch  
- `git switch -c <branch>` – Create and switch  
- `git log --oneline --graph --all` – View branch tree  
- `git branch -d <branch-name>` – Delete a branch

---

## Merge
- `git merge <branch>` – Merge into current
- Fast-forward vs true merge
- Merge conflicts – resolved manually
- `git commit` to finalize after conflict

---

## Rebase
- `git rebase <branch>` – Replay commits
- Rewrites history
- Safer to use on local branches
- Avoid rebasing public history

---

## Reset
- `git reset --soft <commit>` – Keep changes staged  
- `git reset --mixed <commit>` – Keep changes unstaged  
- `git reset --hard <commit>` – Discard all changes  
- Dangerous but powerful

---

## Remote
- `git remote -v` – Show remotes
- `git remote add origin <url>`  
- `git push -u origin main` – Push and set upstream
- `git pull` – Fetch and merge
- `git fetch` – Only fetch
- `git clone <url>` – Copy remote repo
- `git remote remove <name>` – Delete a remote

---

## GitHub
TODO:
- SSH vs HTTPS
- Pull Requests
- Forks and Contributions
- GitHub Actions
- Repos, Issues, Discussions
- Personal Access Tokens

---

## Gitignore
TODO:
- `.gitignore` syntax
- Ignoring specific files/folders
- Using global gitignore
- Common ignore patterns
