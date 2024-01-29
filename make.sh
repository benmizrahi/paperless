next_version=$(bump-my-version show new_version --increment minor)
echo "Next version: $next_version"
bump-my-version bump minor setup.py
echo $next_version >> VERSION