def validate_input(user_input):
    '''
    Function validates user input. 
    Returns True if input is valid, 
    False if input is invalid. 
    '''
    if len(user_input) != 1:
        return False
    

def format_event(event):
    '''
    Function converts the data in the event dictionary to a sentence. 
    Takes a dictionary from the GitHub API call, 
    returns a string describing the event in plain text.
    '''
    event_type = event.get("type", "UnknownEvent")
    repo = event.get("repo", {}).get("name", "unknown repository")
    payload = event.get("payload", {})

    if event_type == "PushEvent":
        commit_count = payload.get("size") or len(payload.get("commits", []))
        if commit_count:
            return f"Pushed {commit_count} commit(s) to {repo}"
        else:
            return f"Pushed commits to {repo}"
    elif event_type == "IssuesEvent":
        action = payload.get("action", "unknown action")
        return f"{action.capitalize()} an issue in {repo}"
    elif event_type == "IssueCommentEvent":
        return f"Commented on an issue in {repo}"
    elif event_type == "WatchEvent":
        return f"Starred {repo}"
    elif event_type == "ForkEvent":
        return f"Forked {repo}"
    elif event_type == "PullRequestEvent":
        action = payload.get("action", "unknown action")
        return f"{action.capitalize()} a pull request in {repo}"
    elif event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "unknown ref type")
        return f"Created {ref_type} in {repo}"
    else:
        return f"{event_type} in {repo}"
