# GIT CHEAT SHEET

---

## Basic Commands
- **Initialize a repository**:  
    ```bash
    git init
    ```
- **Clone a repository**:  
    ```bash
    git clone <repository-url>
    ```
- **Check repository status**:  
    ```bash
    git status
    ```

## Working with Changes
- **Stage changes**:  
    ```bash
    git add <file>
    ```
- **Stage all changes**:  
    ```bash
    git add .
    ```
- **Commit changes**:  
    ```bash
    git commit -m "Commit message"
    ```
- **Amend last commit**:  
    ```bash
    git commit --amend
    ```

## Branching
- **List branches**:  
    ```bash
    git branch
    ```
- **Create a new branch**:  
    ```bash
    git branch <branch-name>
    ```
- **Switch to a branch**:  
    ```bash
    git checkout <branch-name>
    ```
- **Create and switch to a branch**:  
    ```bash
    git checkout -b <branch-name>
    ```
- **Delete a branch**:  
    ```bash
    git branch -d <branch-name>
    ```

## Merging and Rebasing
- **Merge a branch**:  
    ```bash
    git merge <branch-name>
    ```
- **Rebase a branch**:  
    ```bash
    git rebase <branch-name>
    ```

## Remote Repositories
- **Add a remote**:  
    ```bash
    git remote add origin <repository-url>
    ```
- **List remotes**:  
    ```bash
    git remote -v
    ```
- **Push changes**:  
    ```bash
    git push origin <branch-name>
    ```
- **Pull changes**:  
    ```bash
    git pull origin <branch-name>
    ```

## Undoing Changes
- **Unstage changes**:  
    ```bash
    git reset <file>
    ```
- **Discard changes**:  
    ```bash
    git checkout -- <file>
    ```
- **Revert a commit**:  
    ```bash
    git revert <commit-hash>
    ```

## Viewing History
- **View commit history**:  
    ```bash
    git log
    ```
- **View a specific file's history**:  
    ```bash
    git log <file>
    ```
- **Show changes**:  
    ```bash
    git diff
    ```

## Stashing
- **Stash changes**:  
    ```bash
    git stash
    ```
- **Apply stashed changes**:  
    ```bash
    git stash apply
    ```
- **List stashes**:  
    ```bash
    git stash list
    ```

## Tags
- **Create a tag**:  
    ```bash
    git tag <tag-name>
    ```
- **Push tags**:  
    ```bash
    git push origin --tags
    ```

## Configuration
- **Set username**:  
    ```bash
    git config --global user.name "Your Name"
    ```
- **Set email**:  
    ```bash
    git config --global user.email "your.email@example.com"
    ```
