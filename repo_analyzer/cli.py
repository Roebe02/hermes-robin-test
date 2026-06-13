#!/usr/bin/env python3
"""
GitHub Repo Analyzer CLI - Advanced Version
"""

import sys
from pathlib import Path
from main import RepoAnalyzer

def main():
    if len(sys.argv) < 2:
        print("📊 GitHub Repo Analyzer")
        print("=" * 50)
        print("\n🚀 Usage:")
        print("  python cli.py <repo_path>      Analyzeriere ein Repo")
        print("  python cli.py .                 Analyzeriere aktuelles Verzeichnis")
        print("\n📈 Output:")
        print("  - Datei-Statistiken")
        print("  - Sprach-Verteilung")
        print("  - Git-Metriken")
        print("  - Contributor-Info")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    
    if repo_path == ".":
        repo_path = str(Path.cwd())
    
    if not Path(repo_path).exists():
        print(f"❌ Repo nicht gefunden: {repo_path}")
        sys.exit(1)
    
    analyzer = RepoAnalyzer(repo_path)
    analyzer.analyze()

if __name__ == '__main__':
    main()
