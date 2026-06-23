#!/usr/bin/env bash
set -e

REPO_NAME="interview-prep-coach"
GITHUB_USER="saurav4geeks"

echo "=== Interview Prep Coach — GitHub Push Script ==="
echo ""

cd "$(dirname "$0")"

# Step 1: Create the GitHub repo
if command -v gh &>/dev/null && gh auth status &>/dev/null 2>&1; then
  echo "✓ GitHub CLI found and authenticated — creating repo..."
  gh repo create "$GITHUB_USER/$REPO_NAME" --public --source=. --remote=origin --push || true
  # gh --source pushes the current branch; we'll push saurav-custom separately
  CREATED=true
else
  echo "GitHub CLI not found or not authenticated."
  echo ""
  echo "Option A — Paste your GitHub Personal Access Token (classic, with 'repo' scope):"
  read -rsp "Token: " GH_TOKEN
  echo ""

  # Create repo via API
  RESPONSE=$(curl -s -o /tmp/gh_create_response.json -w "%{http_code}" \
    -X POST "https://api.github.com/user/repos" \
    -H "Authorization: token $GH_TOKEN" \
    -H "Accept: application/vnd.github+json" \
    -d "{\"name\":\"$REPO_NAME\",\"private\":false}")

  if [ "$RESPONSE" = "201" ]; then
    echo "✓ Repo created successfully."
  else
    echo "API response: $RESPONSE"
    cat /tmp/gh_create_response.json
    echo ""
    echo "If repo already exists, continuing with push..."
  fi

  # Configure remote with token auth
  git remote remove origin 2>/dev/null || true
  git remote add origin "https://$GH_TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git"
  CREATED=false
fi

# Step 2: Push main
echo ""
echo "Pushing main branch..."
git push -u origin main

# Step 3: Push saurav-custom
echo "Pushing saurav-custom branch..."
git push origin saurav-custom

echo ""
echo "✓ Done! Both branches are live:"
echo "  https://github.com/$GITHUB_USER/$REPO_NAME/tree/main"
echo "  https://github.com/$GITHUB_USER/$REPO_NAME/tree/saurav-custom"
