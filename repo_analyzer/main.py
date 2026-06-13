#!/usr/bin/env python3
"""
GitHub Repo Analyzer - Analyzeriere Repos und zeige Statistiken
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

class RepoAnalyzer:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.stats = {
            'total_files': 0,
            'total_lines': 0,
            'languages': defaultdict(int),
            'commits': 0,
            'branches': 0,
            'contributors': 0,
        }
    
    def analyze(self):
        """Führe komplette Analyse aus"""
        print(f"🔍 Analysiere: {self.repo_path.name}")
        print("=" * 50)
        
        self._count_files_and_lines()
        self._get_git_stats()
        self._print_results()
    
    def _count_files_and_lines(self):
        """Zähle Dateien und Lines of Code"""
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}
        
        for dirpath, dirnames, filenames in os.walk(self.repo_path):
            # Filter excluded dirs
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            
            for filename in filenames:
                # Skip certain files
                if filename.startswith('.'):
                    continue
                
                filepath = Path(dirpath) / filename
                ext = filepath.suffix or 'no-ext'
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = len(f.readlines())
                        self.stats['languages'][ext] += lines
                        self.stats['total_lines'] += lines
                        self.stats['total_files'] += 1
                except:
                    pass
    
    def _get_git_stats(self):
        """Hole Git Statistiken"""
        try:
            # Commits
            result = subprocess.run(
                ['git', 'rev-list', '--count', 'HEAD'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            self.stats['commits'] = int(result.stdout.strip()) if result.returncode == 0 else 0
            
            # Branches
            result = subprocess.run(
                ['git', 'branch', '-r'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            self.stats['branches'] = len([l for l in result.stdout.strip().split('\n') if l])
            
            # Contributors
            result = subprocess.run(
                ['git', 'shortlog', '-sn', 'HEAD'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            self.stats['contributors'] = len([l for l in result.stdout.strip().split('\n') if l])
        except:
            pass
    
    def _print_results(self):
        """Zeige Ergebnisse"""
        print(f"\n📊 **STATISTIKEN**")
        print(f"  Dateien:      {self.stats['total_files']}")
        print(f"  Zeilen Code:  {self.stats['total_lines']:,}")
        print(f"  Commits:      {self.stats['commits']}")
        print(f"  Branches:     {self.stats['branches']}")
        print(f"  Contributors: {self.stats['contributors']}")
        
        print(f"\n📝 **SPRACHEN**")
        sorted_langs = sorted(
            self.stats['languages'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        for ext, lines in sorted_langs:
            percent = (lines / self.stats['total_lines'] * 100) if self.stats['total_lines'] > 0 else 0
            print(f"  {ext:20} {lines:8,} lines ({percent:5.1f}%)")
        
        print("\n" + "=" * 50)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <repo_path>")
        sys.exit(1)
    
    analyzer = RepoAnalyzer(sys.argv[1])
    analyzer.analyze()
