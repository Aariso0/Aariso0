#!/usr/bin/env python3
"""Refresh the recently pushed repositories section in the profile README."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

USERNAME = os.environ.get("GITHUB_USERNAME", "Aariso0")
MAX_REPOSITORIES = 5
PER_PAGE = 100
README_PATH = Path(__file__).resolve().parents[1] / "README.md"
START_MARKER = "<!-- RECENT_REPOS_START -->"
END_MARKER = "<!-- RECENT_REPOS_END -->"
INDIA_TIME = ZoneInfo("Asia/Kolkata")


def escape_markdown(value: str) -> str:
    """Escape characters that can affect Markdown table/list rendering."""
    value = value.replace("\\", "\\\\")
    for char in ("`", "*", "_", "[", "]", "|"):
        value = value.replace(char, f"\\{char}")
    return value


def fetch_repositories() -> list[dict]:
    """Fetch the newest pushed public repositories owned by the profile user."""
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Aariso0-profile-readme-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repositories: list[dict] = []
    page = 1

    while len(repositories) < MAX_REPOSITORIES:
        url = (
            f"https://api.github.com/users/{quote(USERNAME, safe='')}/repos"
            f"?type=owner&sort=pushed&direction=desc&per_page={PER_PAGE}&page={page}"
        )
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            batch = json.loads(response.read().decode("utf-8"))

        if not isinstance(batch, list):
            raise RuntimeError("GitHub API returned an unexpected response.")

        for repo in batch:
            # Keep the list focused on original, active repositories owned by Aariso0.
            if repo.get("fork") or repo.get("archived"):
                continue
            if not repo.get("pushed_at") or not repo.get("html_url"):
                continue
            repositories.append(repo)
            if len(repositories) == MAX_REPOSITORIES:
                break

        if len(batch) < PER_PAGE:
            break
        page += 1

    return repositories


def render_repositories(repositories: list[dict]) -> str:
    if not repositories:
        return "_No non-fork, non-archived public repositories found yet._"

    lines = []
    for repo in repositories:
        name = escape_markdown(repo.get("name") or repo["full_name"])
        url = repo["html_url"]
        description = (repo.get("description") or "No description added yet.").replace("\r", " ").replace("\n", " ").strip()
        if len(description) > 140:
            description = description[:137].rstrip() + "..."
        description = escape_markdown(description)

        language = repo.get("language")
        language_text = f" · `{escape_markdown(language)}`" if language else ""
        pushed_at = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
        pushed_local = pushed_at.astimezone(INDIA_TIME).strftime("%d %b %Y, %I:%M %p IST")

        lines.append(
            f"- **[{name}]({url})** — {description}{language_text} · pushed {pushed_local}"
        )

    return "\n".join(lines)


def update_readme(content: str) -> bool:
    readme = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"({re.escape(START_MARKER)})(.*?)({re.escape(END_MARKER)})",
        flags=re.DOTALL,
    )
    matches = list(pattern.finditer(readme))
    if len(matches) != 1:
        raise RuntimeError(
            "README.md must contain exactly one RECENT_REPOS_START / RECENT_REPOS_END marker pair."
        )

    replacement = f"{START_MARKER}\n\n{content}\n\n{END_MARKER}"
    updated = pattern.sub(lambda _match: replacement, readme, count=1)
    if updated == readme:
        return False

    README_PATH.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    try:
        repos = fetch_repositories()
        changed = update_readme(render_repositories(repos))
        print("README updated." if changed else "README is already up to date.")
        return 0
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError, RuntimeError) as exc:
        print(f"Failed to update recent repositories: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
