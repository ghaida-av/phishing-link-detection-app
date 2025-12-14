#!/bin/bash

echo "🚀 GitHub Setup Script for Phishing Link Detection App"
echo "====================================================="
echo ""

# 1. Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Install it from: https://git-scm.com/downloads"
    exit 1
fi
echo "✅ Git is installed"
echo ""

# 2. Initialize Git repo if not present
if [ -d ".git" ]; then
    echo "✅ Git repo already initialized"
    git status --short | head -5
else
    echo "📦 Creating new Git repo..."
    git init
    echo "✅ Git repo created"
fi
echo ""

# 3. Check for remote
REMOTE=$(git remote get-url origin 2>/dev/null)
if [ -z "$REMOTE" ]; then
    echo "⚠️  No GitHub remote found."
    echo "Run these commands after creating a repo on GitHub:"
    echo "  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo "  git push -u origin main"
else
    echo "✅ Remote connected: $REMOTE"
fi
echo ""

# 4. Check for commits
if [ -z "$(git log --oneline -1 2>/dev/null)" ]; then
    echo "📝 No commits yet."
    echo "Run:"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo "  git push -u origin main"
else
    echo "✅ Last commit:"
    git log --oneline -1
fi
echo ""

# 5. Check uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📋 Uncommitted changes:"
    git status --short | head -10
    echo ""
    echo "To save changes:"
    echo "  git add ."
    echo "  git commit -m 'Update files'"
    echo "  git push"
else
    echo "✅ All changes are saved"
fi
echo ""

# 6. Check for GitHub Actions workflow (optional for Android build)
if [ -f ".github/workflows/build-apk.yml" ]; then
    echo "✅ GitHub Actions workflow found:"
    echo "   .github/workflows/build-apk.yml"
else
    echo "⚠️  No GitHub Actions workflow found"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━"
echo "📘 Next Steps"
echo "━━━━━━━━━━━━━━━━━━━━━━"
echo "1. Create a new repo on GitHub."
echo "2. Connect it:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "3. Push your code:"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git push -u origin main"
echo "4. (Optional) Set up GitHub Actions to automate Android build and ML deployment"
echo "5. (Optional) Download APK or ML artifacts from GitHub Actions artifacts"
echo ""

echo "✅ Setup Complete!"



