#!/usr/bin/env python3
"""
GitHub Repo Analyzer Web API
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
import shutil
from pathlib import Path
import sys

# Add parent dir to path für main.py import
sys.path.insert(0, str(Path(__file__).parent))
from main import RepoAnalyzer

app = FastAPI(
    title="🔍 GitHub Repo Analyzer API",
    description="Analyzeriere GitHub Repos via Web Interface",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve HTML
    with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'r') as f:
        return f.read()

@app.post("/api/analyze")
async def analyze_repo(url: str = None, file: UploadFile = File(None)):
    """Analyzeriere ein Repo von URL oder Upload"""
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        if url:
            # Git clone from URL
            import subprocess
            result = subprocess.run(
                ['git', 'clone', url, temp_dir],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode != 0:
                raise HTTPException(status_code=400, detail=f"Git clone failed: {result.stderr}")
        
        elif file:
            # Handle uploaded file
            if file.filename.endswith('.zip'):
                import zipfile
                zip_path = os.path.join(temp_dir, 'repo.zip')
                with open(zip_path, 'wb') as f:
                    f.write(await file.read())
                
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                os.remove(zip_path)
            else:
                raise HTTPException(status_code=400, detail="Only .zip files supported")
        else:
            raise HTTPException(status_code=400, detail="Provide either url or file")
        
        # Find the actual repo directory (handle nested folders)
        repo_dir = temp_dir
        subdirs = [d for d in os.listdir(temp_dir) if os.path.isdir(os.path.join(temp_dir, d))]
        if len(subdirs) == 1 and not os.path.exists(os.path.join(temp_dir, '.git')):
            repo_dir = os.path.join(temp_dir, subdirs[0])
        
        # Run analyzer
        analyzer = RepoAnalyzer(repo_dir)
        analyzer.analyze()
        
        # Convert to dict
        result = {
            "success": True,
            "stats": {
                "total_files": analyzer.stats['total_files'],
                "total_lines": analyzer.stats['total_lines'],
                "commits": analyzer.stats['commits'],
                "branches": analyzer.stats['branches'],
                "contributors": analyzer.stats['contributors'],
                "languages": dict(sorted(
                    analyzer.stats['languages'].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10])
            }
        }
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # Cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)

@app.get("/api/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
