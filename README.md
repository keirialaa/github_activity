# GitHub User Activity CLI

A command-line tool that fetches and displays the recent public activity of any GitHub user, using the GitHub Events API.

## Features

- Fetches the most recent public activity for any GitHub user
- Displays activity in plain, readable text
- Handles common errors gracefully (invalid username, network issues, API rate limits)

## Requirements

- Python 3.12+
- Dependencies are installed automatically via `pip install -e .`

## Installation

```bash
git clone https://github.com/keirialaa/github-activity
cd github-activity
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

## Usage

```bash
python src/github_activity/main.py <username>
```

## Example Output

```
$ github-activity keirialaa

Opened a pull request in my_project
Pushed commits to keirialaa/my_project
Forked my_project
Opened a pull request in my_project
Pushed commits to keirialaa/my_project
```

## Error Handling

The tool handles the following cases:

- **User not found** — displays a clear message if the username does not exist
- **Rate limit exceeded** — GitHub allows 60 unauthenticated requests per hour
- **Network error** — displays a message if GitHub cannot be reached
- **No recent activity** — displays a message if the user has no public events

## Limitations

The GitHub Events API returns a maximum of 300 events, covering up to the last 90 days of public activity.
