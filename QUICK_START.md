# ⚡ Quick Start (30 Seconds)

## Three tiny things:

### 1. GitHub PAT
```
→ github.com/settings/tokens
→ Fine-grained tokens
→ Tick "Contents: read/write"
→ Copy token
→ Add to .env:
```
```env
GITHUB_PAT=ghp_...
```

### 2. Ollama Running
```bash
# In Termux:
bash
ollama serve &
ollama pull qwen2.5-coder:14b
```
*(Fits on any phone with 12GB RAM)*

### 3. Launch Script
Already created: `launch.sh`

Make it runnable (if not already):
```bash
chmod +x launch.sh
```

## Run It
```bash
./launch.sh Make a todo app with drag-drop
```

**Boom—Pantheon boots, agents loop, code builds, GitHub pushes, preview at `localhost:8080`.**

---

## No Cloud Keys Needed
Just the GitHub PAT above. Everything else runs locally.

## Skip Python?
The web UI works standalone:
```bash
pkg install nodejs
npm start
```
Then visit `http://localhost:3001` and paste your API key.

---

**Status:** Ready to manifest. 🔥⚡
