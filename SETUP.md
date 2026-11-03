# Aariso0 GitHub profile setup

This pack contains a profile README plus a GitHub Actions job that keeps the
"Recently pushed repositories" section sorted by latest push.

## Install

1. Create a **public** repository named exactly `Aariso0` if it does not already exist.
2. Copy `README.md`, the `.github/` directory, and the `scripts/` directory into the repository root.
3. Commit and push the files to the repository's default branch.
4. Open **Settings → Actions → General → Workflow permissions**. Allow read and write access to the repository contents if the workflow is blocked from pushing its update.
5. Open **Actions → Update recent repositories → Run workflow** once to populate the section immediately.

The workflow then runs every six hours. GitHub scheduled workflows use UTC; the generated push timestamps are displayed in India Standard Time.

## What the updater does

- Calls GitHub's public user-repositories REST endpoint for `Aariso0`.
- Requests repositories ordered by `pushed` in descending order.
- Displays the five newest repositories owned by the account.
- Skips forks and archived repositories.
- Uses the repository's latest `pushed_at` timestamp, displayed in IST.
- Updates only the content between `RECENT_REPOS_START` and `RECENT_REPOS_END` in `README.md`.
- Commits only when the README actually changes.

No personal access token or third-party secret is required for public repositories. The built-in `GITHUB_TOKEN` is used for API requests and the workflow's commit.

## Personalize before publishing

The README's introduction and technology icons are a starting point based on the projects and tools discussed. Remove technologies you do not want to represent publicly, and add a short description/link for any flagship project you want recruiters or contributors to notice. Pin up to six of your strongest repositories manually on your GitHub profile as well; the dynamic recent list is not a replacement for curated pins.
