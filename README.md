# hermes-robin-test

🧪 **Test Repository für Hermes GitHub Integration**

Ein **cooles Projekt** mit dem **GitHub Repo Analyzer** — analyzeriere GitHub Repos und sieh Statistiken!

## 🚀 Features

- ✅ **CLI Tool** — Analyzeriere Repos von der Kommandozeile
- ✅ **Web Interface** — Schöne Web UI mit FastAPI
- ✅ **Git Integration** — Hole Git-Statistiken (Commits, Branches, Contributors)
- ✅ **Language Detection** — Zeige Sprach-Verteilung
- ✅ **Docker Support** — Easy Deployment

## 📊 GitHub Repo Analyzer

### Quick Start (CLI)

```bash
# Analyzeriere aktuelles Verzeichnis
cd repo_analyzer
python main.py .

# Analyzeriere ein Repo
python main.py /path/to/repo
```

### Web Interface

```bash
# Install dependencies
pip install -r repo_analyzer/requirements.txt

# Start server
python repo_analyzer/app.py

# Open browser
open http://localhost:8000
```

### Docker

```bash
docker-compose up
# Open http://localhost:8000
```

## 📈 Output Example

```
🔍 Analysiere: hermes-robin-test
============================================================
📊 STATISTIKEN
  Dateien:      10
  Zeilen Code:  1,243
  Commits:      5
  Branches:     3
📝 SPRACHEN
  .py                  ████████████░░░░░░░░ 64.3%
  .html                ███░░░░░░░░░░░░░░░░░ 15.2%
  .json                ██░░░░░░░░░░░░░░░░░░ 10.5%
============================================================
```

## 🌳 Features zum Testen

- [x] Basic commits & branches
- [x] Feature branches (colored-output)
- [x] CLI Tool mit Progress Bars
- [x] FastAPI Web Interface
- [x] Docker Support
- [ ] PRs & Issues
- [ ] Releases
- [ ] CI/CD Workflows

## 🛠️ Tech Stack

- **Backend**: FastAPI + Python 3.11
- **Frontend**: HTML5 + CSS3 + Vanilla JS
- **Deployment**: Docker + Docker Compose
- **VCS**: Git + GitHub

## 📝 File Structure

```
hermes-robin-test/
├── repo_analyzer/
│   ├── main.py           # Core analyzer logic
│   ├── cli.py            # CLI interface
│   ├── app.py            # FastAPI app
│   ├── index.html        # Web UI
│   ├── requirements.txt   # Dependencies
│   ├── setup.py          # Setup script
│   ├── Dockerfile        # Docker image
│   └── README.md         # Tool docs
├── docker-compose.yml    # Docker Compose
├── README.md            # This file
└── .git/                # Git history
```

## 🚀 Roadmap

- [ ] JSON Export
- [ ] Trend Analytics
- [ ] GitHub API Integration
- [ ] Advanced Filtering
- [ ] Report Generation
- [ ] Web Dashboard Improvements

---

Made with ❤️ by Robin + Hermes 🔥
