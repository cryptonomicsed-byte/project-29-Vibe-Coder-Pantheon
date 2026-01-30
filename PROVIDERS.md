# 🔌 Supported LLM Providers

The Vibe Coder Pantheon supports 8+ LLM providers. Choose any that fits your needs.

## Providers Matrix

| Provider | Free Trial | Cost | Speed | Quality | Best For |
|----------|-----------|------|-------|---------|----------|
| **OpenAI (GPT-3.5)** | ✅ $5 | Pay-per-use | Medium | Excellent | General purpose, best overall |
| **Claude (Anthropic)** | ✅ Free tier | Pay-per-use | Medium | Excellent | Long context, reasoning |
| **Gemini (Google)** | ✅ Free | Free/Pay | Fast | Very Good | Fast, cost-effective |
| **Mistral** | ✅ Free | Pay-per-use | Fast | Very Good | European, open-source |
| **Groq** | ✅ Free | Free | ⚡ FASTEST | Good | Speed-optimized inference |
| **Perplexity** | ✅ Free | Free tier | Medium | Good | Web search + reasoning |
| **Ollama** | ✅ 100% Free | Local | Variable | Good | Full privacy, local |
| **Cohere** | ✅ Free | Free/Pay | Medium | Very Good | Enterprise use |

---

## Setup Instructions

### 1. OpenAI (GPT-3.5-turbo)

**Best for:** General coding, fast, most reliable

1. Go to: https://platform.openai.com/signup
2. Create account and verify email
3. Go to: https://platform.openai.com/api/keys
4. Click "Create new secret key"
5. Copy key (starts with `sk-`)
6. Paste in Pantheon UI, select "OpenAI"

**Cost:** ~$0.001 per 1K tokens (cheap)

---

### 2. Anthropic Claude

**Best for:** Long context, complex reasoning, very creative

1. Go to: https://console.anthropic.com/signup
2. Create account and verify
3. Go to: https://console.anthropic.com/keys
4. Click "Create Key"
5. Copy key (starts with `sk-ant-`)
6. Paste in Pantheon UI, select "Anthropic Claude"

**Cost:** ~$0.003 per 1K tokens (cheapest for long context)

---

### 3. Google Gemini

**Best for:** Speed + quality balance, free tier

1. Go to: https://aistudio.google.com
2. Click "Get API key" (free, no credit card needed)
3. Copy key (starts with `AIza`)
4. Paste in Pantheon UI, select "Google Gemini"

**Cost:** Free tier available, then pay-per-use

---

### 4. Mistral AI

**Best for:** European privacy, open-source option

1. Go to: https://console.mistral.ai
2. Sign up
3. Go to: API Keys section
4. Create new key (starts with `eyJ0eXAi`)
5. Paste in Pantheon UI, select "Mistral"

**Cost:** ~$0.002 per 1K tokens

---

### 5. Groq (⚡ FASTEST)

**Best for:** Speed demons, real-time applications

1. Go to: https://console.groq.com
2. Sign up
3. Go to: API Keys
4. Create key (starts with `gsk_`)
5. Paste in Pantheon UI, select "Groq"

**Cost:** Free tier available

**Note:** Fastest LLM inference available. Perfect for fast code generation.

---

### 6. Perplexity AI

**Best for:** Web search + reasoning (great for research)

1. Go to: https://www.perplexity.ai
2. Sign up or use Google login
3. Go to: Settings → API
4. Create API key (starts with `pplx-`)
5. Paste in Pantheon UI, select "Perplexity"

**Cost:** Free tier available

---

### 7. Ollama (Local, 100% Private)

**Best for:** Privacy-first, offline, zero cost

1. Install Ollama: https://ollama.ai
2. Pull a model:
   ```bash
   ollama pull llama3.1
   # or faster/smaller:
   ollama pull phi  # 2.2GB
   ollama pull mistral  # 4.1GB
   ```
3. Start Ollama:
   ```bash
   ollama serve
   ```
4. In Pantheon UI, select "Ollama (Local)"
5. API Key: Leave blank or use "localhost"

**Cost:** FREE (download model once)

**Pros:**
- 100% private, no data sent to cloud
- Works offline
- Zero API costs
- Full control

**Cons:**
- Runs on your machine (needs good specs)
- Slower than cloud APIs
- Smaller context window

**Recommended Models:**
- `llama3.1` — Best overall (~4.7GB)
- `mistral` — Fast (~4.1GB)
- `phi` — Lightweight (~2.2GB)
- `deepseek-coder` — Code-optimized (~3.8GB)

---

### 8. Cohere

**Best for:** Enterprise, generation tasks

1. Go to: https://dashboard.cohere.com
2. Sign up
3. Go to: API Keys
4. Create key (starts with `sk-`)
5. Paste in Pantheon UI, select "Cohere"

**Cost:** Free tier available

---

## Environment Variables (CLI)

If using command-line mode without web UI:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."
python3 agents_cloud.py

# Claude
export ANTHROPIC_API_KEY="sk-ant-..."
python3 agents_cloud.py

# Gemini
export GOOGLE_API_KEY="AIza..."
python3 agents_cloud.py

# Mistral
export MISTRAL_API_KEY="eyJ0eXAi..."
python3 agents_cloud.py

# Groq
export GROQ_API_KEY="gsk_..."
python3 agents_cloud.py

# Cohere
export COHERE_API_KEY="sk-..."
python3 agents_cloud.py

# Ollama (local)
export OLLAMA_MODEL="llama3.1"
ollama serve  # In separate terminal
python3 agents_simple.py
```

---

## Recommended Combinations

### 🚀 Fast & Free
- **Gemini** (free tier) + **Groq** (fallback)
- Fast iterations, zero cost

### 💎 Best Quality
- **Claude** (Anthropic)
- Most creative, best reasoning

### 🔥 Best for Code
- **OpenAI GPT-4** (if budget allows)
- **Mistral** (good balance)
- **Groq** (fastest)

### 🛡️ Privacy First
- **Ollama** (local, 100% private)
- **Mistral** (EU-based)

### 💰 Budget Conscious
- **Groq** (free tier)
- **Gemini** (free tier)
- **Perplexity** (free tier)

### 🏢 Enterprise
- **Cohere**
- **Claude** (Anthropic)

---

## Cost Comparison (per 1000 tokens)

```
Free Tier:       Groq, Gemini, Perplexity, Ollama
Cheapest Paid:   Mistral ($0.002), Gemini ($0.0003-0.0005)
Mid-Range:       OpenAI ($0.001-0.002), Claude ($0.003)
Premium:         Cohere ($0.005+)
```

**Example:** For a typical vibe (5 agents × 3 phases = 15 requests):
- OpenAI: ~$0.02-0.05
- Claude: ~$0.05-0.10
- Groq: FREE
- Ollama: FREE

---

## Troubleshooting

### "API key invalid"
- Copy-paste the full key (no spaces)
- Check provider website for current key format
- Some providers change key prefixes over time

### "Rate limit exceeded"
- Provider is limiting requests
- Free tier limitations (especially Gemini, Groq)
- Wait a few minutes or upgrade plan

### "Connection timeout (Ollama)"
- Ollama not running: `ollama serve`
- Port 11434 blocked (firewall)
- Model too large for available RAM

### Provider not working?
- Check API key is valid: test on provider's playground
- Check internet connection
- Check provider status page for outages

---

## Adding a New Provider

To add a new LLM provider:

1. **Edit `llm_providers.py`:**
   ```python
   class MyProviderName(LLMProvider):
       def generate(self, prompt: str, max_tokens: int = 1000) -> str:
           # Call your provider's API
           return response_text
   
   PROVIDERS['myprovider'] = MyProviderName
   ```

2. **Update `server.js`:**
   ```javascript
   const PROVIDERS = {
     // ...
     'myprovider': 'My Provider Name'
   };
   ```

3. **Restart server:** `npm start`

4. **Use in UI:** Select from provider dropdown

Done!

---

## FAQ

**Q: Which provider should I pick?**
A: Start with **Groq** (free, fastest) or **Gemini** (free tier). Both require no credit card.

**Q: Can I switch providers mid-way?**
A: Yes! Just configure a new key and submit a new vibe.

**Q: Is Ollama slow?**
A: Compared to cloud APIs, yes. But privacy is worth it. Use smaller models (phi, mistral) for speed.

**Q: Can I use multiple providers in one vibe?**
A: Not yet, but it's planned! Currently one provider per Pantheon session.

**Q: Will my code be stored?**
A: Only locally in `pantheon_results.json`. Depends on provider (read their privacy policy).

---

🔌 **Pick a provider. Start your vibe. Let the Pantheon code.**
