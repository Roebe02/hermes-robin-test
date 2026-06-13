# 📊 GitHub Repo Analyzer

Ein **geiles** Python CLI Tool zum Analysieren von GitHub Repositories.

## Features 🚀

- 📁 Zählt **alle Dateien** und **Lines of Code**
- 📝 Zeigt **Sprach-Verteilung** (Python, JS, Go, etc.)
- 🔗 Holt **Git-Statistiken** (Commits, Branches, Contributors)
- ⚡ **Super schnell** auch bei großen Repos
- 🎨 **Nice formatted Output**

## Installation

```bash
# Klone das Repo
git clone https://github.com/Roebe02/hermes-robin-test.git
cd hermes-robin-test/repo_analyzer

# Install (optional)
pip install -e .
```

## Usage

```bash
# Analyzeriere aktuelles Verzeichnis
python main.py .

# Analyzeriere spezifisches Repo
python main.py /path/to/repo

# Mit CLI
python cli.py .
```

## Output Beispiel

```
🔍 Analysiere: hermes-robin-test
==================================================

📊 **STATISTIKEN**
  Dateien:      5
  Zeilen Code:  421
  Commits:      3
  Branches:     2
  Contributors: 1

📝 **SPRACHEN**
  .py                       240 lines (57.0%)
  .md                        89 lines (21.1%)
  .json                      92 lines (21.9%)

==================================================
```

## Was kann man damit machen? 🎯

- 📊 Repo-Größe schnell checken
- 🔍 Sprach-Verteilung analysieren
- 📈 Git-Historie untersuchen
- 🚀 Größte Repos finden
- 📝 Automatisierte Reports generieren

## Zukünftige Features ✨

- [ ] JSON Export
- [ ] Trend-Analyse (über Zeit)
- [ ] GitHub API Integration
- [ ] Web Dashboard
- [ ] Docker Support

---

Made with 🔥 by Robin + Hermes
