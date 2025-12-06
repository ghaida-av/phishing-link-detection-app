#!/bin/bash

echo "🚀 GitHub Setup Helper Script"
echo "=============================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed."
    echo "Please install Git first: https://git-scm.com/downloads"
    exit 1
fi

echo "✅ Git is installed"
echo ""

# Check if already a git repository
if [ -d ".git" ]; then
    echo "✅ Git repository already initialized"
    git status --short | head -5
    echo ""
else
    echo "📦 Initializing git repository..."
    git init
    echo "✅ Git repository initialized"
    echo ""
fi

# Check if remote is set
REMOTE=$(git remote get-url origin 2>/dev/null)

if [ -z "$REMOTE" ]; then
    echo "⚠️  No GitHub remote configured"
    echo ""
    echo "To connect to GitHub:"
    echo "1. Create a repository on GitHub.com"
    echo "2. Then run:"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo "   git push -u origin main"
    echo ""
else
    echo "✅ GitHub remote configured: $REMOTE"
    echo ""
fi

# Check if files are committed
if [ -z "$(git log --oneline -1 2>/dev/null)" ]; then
    echo "📝 No commits yet. Ready to commit files..."
    echo ""
    echo "To commit and push:"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo "  git push -u origin main"
    echo ""
else
    echo "✅ Repository has commits"
    LAST_COMMIT=$(git log --oneline -1)
    echo "   Latest: $LAST_COMMIT"
    echo ""
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📋 You have uncommitted changes:"
    git status --short | head -10
    echo ""
    echo "To commit them:"
    echo "  git add ."
    echo "  git commit -m 'Update files'"
    echo "  git push"
    echo ""
else
    echo "✅ All changes are committed"
    echo ""
fi

# Check if GitHub Actions workflow exists
if [ -f ".github/workflows/build-apk.yml" ]; then
    echo "✅ GitHub Actions workflow file exists"
    echo "   Location: .github/workflows/build-apk.yml"
    echo ""
else
    echo "⚠️  GitHub Actions workflow not found"
    echo ""
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📖 Next Steps:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Create repository on GitHub.com"
echo "2. Connect it:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo ""
echo "3. Push code:"
echo "   git add ."
echo "   git commit -m 'Initial commit'"
echo "   git push -u origin main"
echo ""
echo "4. Go to GitHub → Actions tab → Run workflow"
echo "5. Download APK from Artifacts"
echo ""
echo "📚 See GITHUB_SETUP_GUIDE.md for detailed instructions"
echo ""

