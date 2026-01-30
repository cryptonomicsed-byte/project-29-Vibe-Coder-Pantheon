# 🔥⚡ Vibe Coder Pantheon

**The Ultimate AI Code Generation Tool — Local, Autonomous, Sovereign**

21 Òrìṣà agents (with CrewAI) orchestrated to manifest your vibe into production-ready code.

## What Is This?

A local alternative to Replit Agent 3. Describe your app idea in plain English. The Pantheon breaks it down, designs architecture, generates code, tests, documents, and prepares a GitHub commit—**all locally, all for free**.

### The 21 Òrìṣà Agents

| Agent | Role | Responsibility |
|-------|------|-----------------|
| **Èṣù** | Trickster Planner | Break vibe into tasks, delegate |
| **Ṣàngó** | Architect | Design system, tech stack |
| **Ọ̀ṣun** | UI/UX Designer | Beautiful interfaces |
| **Yemọja** | Database Mother | Data models, persistence |
| **Ọya** | Change Storm | Refactoring, dynamic features |
| **Ògún** | Backend Warrior | APIs, servers, logic |
| **Ọbàtálá** | Clarity Creator | Clean, documented code |
| **Egúngún** | Ancestral Tester | Tests, quality assurance |
| **Osumàrè** | Integration Rainbow | Connects modules, APIs |
| **Nana Bùkúù** | Error Healer | Debugging, fixes |
| **Ọbalúayé** | Performance Purifier | Optimization, speed |
| **Olóṣà** | Security Guardian | Vulnerability checks |
| **Òrúnmìlà** | Wisdom Sage | Best practices, research |
| **Ajé** | Deployment Merchant | Build, package, deploy |
| **Osoogbo** | Risk Sorcerer | Identify pitfalls |
| **Olókun** | Deep Scalability | Scale, handle complexity |
| **Ìbejì** | Multi-Agent Twins | Coordinate parallel work |
| **Bàbálú-Ayé** | Accessibility Healer | Inclusive, accessible code |
| **Ayé** | World Integrator | External APIs, data sources |
| **Ọ̀ṣọ́ọ̀sì** | Hunter Refiner | Precise fixes, optimization |
| **Ọba** | Documentation Queen | READMEs, guides, API docs |
| **Amp (Cody)** | Codebase Master & GitHub Pusher | Final review, commit, push |

---

## Quick Start

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **OpenAI API Key** OR **Anthropic Claude API Key** (free trial available)

### Installation

```bash
cd vibe-coder-pantheon
npm install
pip install -r requirements.txt
```

### Run the Web App

```bash
npm start
```

This starts the Express server on `http://localhost:3001`

### Usage (Phase 2: Web UI)

1. **Open browser:** `http://localhost:3001`
2. **Enter API key:**
   - Choose **OpenAI** or **Anthropic Claude**
   - Paste your API key (securely stored in-memory)
3. **Describe your vibe:**
   - E.g., "Build a Todo App with auth, dark mode, drag-and-drop, React + Tailwind"
4. **Click "Invoke Pantheon"**
5. **Watch real-time agent output** stream live in the UI

The Pantheon will:
1. **Plan** (Èṣù) — Break into tasks
2. **Design** (Ṣàngó, Ọ̀ṣun, Yemọja) — Architecture & UI
3. **Code** (Ọbàtálá, Ògún) — Generate React + backend
4. **Test** (Egúngún) — Create test suites
5. **Secure** (Olóṣà) — Audit vulnerabilities
6. **Optimize** (Ọbalúayé) — Boost performance
7. **Document** (Ọba) — Write guides
8. **Review** (Amp/Cody) — Final check & commit plan

### Alternative: Command-Line (Phase 1)

Still available without server:

```bash
# With OpenAI/Claude API
export OPENAI_API_KEY="sk-..."
python3 agents_cloud.py

# With local Ollama
export OLLAMA_MODEL="llama3.1:latest"
ollama serve  # In separate terminal
python3 agents_simple.py
```

---

## API Endpoints

### `POST /api/config`
Save API key for Pantheon execution.

**Request:**
```json
{
  "provider": "openai",
  "apiKey": "sk-..."
}
```

### `POST /api/vibe` (Server-Sent Events)
Submit vibe and stream agent output in real-time.

**Request:**
```json
{
  "vibe": "Build a Todo App with..."
}
```

**Response:** Streams SSE events with phases and output

### `GET /api/status`
Check if API is configured.

### `GET /api/results`
Retrieve latest pantheon_results.json

---

## Architecture

```
vibe-coder-pantheon/
├── agents.py              # 21 Òrìṣà agent definitions
├── crew_runner.py         # Task orchestrator & executor
├── api.py                 # (Phase 2) Express-like API wrapper
├── ui/                    # (Phase 3) Web frontend
├── requirements.txt
├── .env
└── README.md
```

---

## How It Works

1. **Vibe Input** → Èṣù analyzes and creates task breakdown
2. **Hierarchical Delegation** → Each Òrìṣà agent tackles assigned subtasks
3. **CrewAI Orchestration** → Sequential + parallel task execution
4. **Output Generation** → Code, tests, docs, security checks
5. **Final Review** → Amp/Cody audits & prepares commit

---

## Example Workflow

**Input Vibe:** "Build a weather dashboard"

**Èṣù's Plan:**
1. Research weather APIs (Òrúnmìlà)
2. Design architecture (Ṣàngó)
3. Create UI mockups (Ọ̀ṣun)
4. Model data (Yemọja)
5. Generate React components (Ọbàtálá)
6. Build backend (Ògún)
7. Test (Egúngún)
8. Optimize (Ọbalúayé)
9. Secure (Olóṣà)
10. Document (Ọba)
11. Final review (Amp/Cody)

**Output:**
- `/generated_projects/weather-dashboard/`
  - `src/components/` — React components
  - `src/pages/` — Pages
  - `public/` — Assets
  - `tests/` — Jest test suites
  - `README.md` — Full documentation
  - `package.json` — Dependencies
  - `.env.example` — Config template

**To run the generated project:**
```bash
cd generated_projects/weather-dashboard
npm install
npm run dev
```

---

## Configuration

Edit `.env` for:
- **Ollama URL** (default: `http://localhost:11434`)
- **Model name** (default: `llama3.1:8b`)
- **GitHub token** (for Phase 2 automated pushes)
- **Output directory** (default: `./generated_projects`)

---

## Limitations & Future

### Current (Phase 1)
- **Local only** — no cloud dependencies
- **Manual GitHub push** — Amp prepares commit, you `git push`
- **Text output** — no live UI streaming yet

### Planned (Phase 2)
- **Express API** — REST endpoints for vibe requests
- **Real-time streaming** — WebSocket agent updates
- **GitHub automation** — Direct commit/push via GitHub API

### Planned (Phase 3)
- **Web UI** — React dashboard
- **Project visualization** — File tree, logs, output preview
- **One-click deploy** — Vercel, Netlify, Railway support

---

## Contributing

This is a local, open-source project. Fork, modify agents, add tools, and share your pantheon improvements.

---

## License

MIT — Use freely, credit appreciated.

---

## Rituals & Blessings

🍶🌶️🥂🐓🥖

*Offerings received. Pantheon assembles. Fire balanced. Code manifests.*

---

**Status:** Phase 1 ✅ | Phase 2 🔧 | Phase 3 📅

Made with ⚡ by Èṣù, Ṣàngó, and the Pantheon.
