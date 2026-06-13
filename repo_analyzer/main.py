#!/usr/bin/env python3
"""
GitHub Repo Analyzer - Main with Colored Output
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def safe(text, color):
        if sys.stdout.isatty():
            return color + str(text) + Colors.ENDC
        return str(text)

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
        print(Colors.safe('🔍 Analysiere: ', Colors.CYAN) + Colors.safe(self.repo_path.name, Colors.BOLD))
        print(Colors.safe("=" * 60, Colors.BLUE))
        
        self._count_files_and_lines()
        self._get_git_stats()
        self._print_results()
    
    def _count_files_and_lines(self):
        exclude_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'dist', 'build'}
        
        for dirpath, dirnames, filenames in os.walk(self.repo_path):
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
            
            for filename in filenames:
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
        try:
            result = subprocess.run(
                ['git', 'rev-list', '--count', 'HEAD'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            self.stats['commits'] = int(result.stdout.strip()) if result.returncode == 0 else 0
            
            result = subprocess.run(
                ['git', 'branch', '-r'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            self.stats['branches'] = len([l for l in result.stdout.strip().split('\n') if l])
            
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
        print(Colors.safe('📊 STATISTIKEN', Colors.GREEN + Colors.BOLD))
        print('  ' + Colors.safe('Dateien:', Colors.YELLOW) + '      ' + Colors.safe(str(self.stats['total_files']), Colors.CYAN))
        print('  ' + Colors.safe('Zeilen Code:', Colors.YELLOW) + '  ' + Colors.safe(str(self.stats['total_lines']), Colors.CYAN))
        print('  ' + Colors.safe('Commits:', Colors.YELLOW) + '      ' + Colors.safe(str(self.stats['commits']), Colors.CYAN))
        print('  ' + Colors.safe('Branches:', Colors.YELLOW) + '     ' + Colors.safe(str(self.stats['branches']), Colors.CYAN))
        print('  ' + Colors.safe('Contributors:', Colors.YELLOW) + ' ' + Colors.safe(str(self.stats['contributors']), Colors.CYAN))
        
        print(Colors.safe('📝 SPRACHEN', Colors.GREEN + Colors.BOLD))
        sorted_langs = sorted(
            self.stats['languages'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        for ext, lines in sorted_langs:
            percent = (lines / self.stats['total_lines'] * 100) if self.stats['total_lines'] > 0 else 0
            bar_length = int(percent / 5)
            bar = '█' * bar_length + '░' * (20 - bar_length)
            bar_colored = Colors.safe(bar, Colors.GREEN)
            print('  ' + str(ext).ljust(20) + ' ' + bar_colored + ' ' + str(round(percent, 1)) + '%')
        
        print(Colors.safe("=" * 60, Colors.BLUE))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <repo_path>")
        sys.exit(1)
    
    analyzer = RepoAnalyzer(sys.argv[1])
    analyzer.analyze()
