/**
 * Vibe Coder Pantheon - Express API Server
 * Phase 2: API + Web UI with API key input
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// In-memory config (in production, use secure storage)
let config = {
  apiKey: null,
  apiProvider: null,
};

// Supported providers
const PROVIDERS = {
  'openai': 'OpenAI (GPT-3.5/4)',
  'claude': 'Anthropic Claude',
  'gemini': 'Google Gemini',
  'mistral': 'Mistral AI',
  'groq': 'Groq (Fast)',
  'perplexity': 'Perplexity AI',
  'ollama': 'Ollama (Local)',
  'cohere': 'Cohere'
};

// === ENDPOINTS ===

/**
 * GET /api/providers
 * Get list of supported providers
 */
app.get('/api/providers', (req, res) => {
  res.json(PROVIDERS);
});

/**
 * POST /api/config
 * Save API key and provider
 */
app.post('/api/config', (req, res) => {
  const { apiKey, provider } = req.body;
  
  if (!apiKey || !provider) {
    return res.status(400).json({ error: 'Missing apiKey or provider' });
  }
  
  if (!PROVIDERS[provider]) {
    return res.status(400).json({ 
      error: `Unknown provider: ${provider}. Available: ${Object.keys(PROVIDERS).join(', ')}`
    });
  }
  
  config = { apiKey, apiProvider: provider };
  
  res.json({
    success: true,
    message: `API key saved for ${provider}`,
    provider: provider,
    providerName: PROVIDERS[provider]
  });
});

/**
 * POST /api/vibe
 * Run Pantheon with given vibe description
 * Streams results via Server-Sent Events (SSE)
 */
app.post('/api/vibe', (req, res) => {
  const { vibe } = req.body;
  
  if (!vibe) {
    return res.status(400).json({ error: 'Missing vibe description' });
  }
  
  if (!config.apiKey) {
    return res.status(401).json({ error: 'API key not configured' });
  }
  
  // Set headers for SSE
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  
  // Send initial event
  res.write(`data: ${JSON.stringify({
    type: 'start',
    message: `🔥⚡ Pantheon awakens... Processing vibe: ${vibe.substring(0, 50)}...`
  })}\n\n`);
  
  // Spawn Python process to run Pantheon
  const pythonProcess = spawn('python3', ['pantheon_runner.py'], {
    cwd: __dirname,
    env: {
      ...process.env,
      OPENAI_API_KEY: config.apiProvider === 'openai' ? config.apiKey : '',
      ANTHROPIC_API_KEY: config.apiProvider === 'claude' ? config.apiKey : '',
      VIBE_INPUT: vibe,
      SSE_MODE: 'true'
    }
  });
  
  let phaseCount = 0;
  
  pythonProcess.stdout.on('data', (data) => {
    const lines = data.toString().split('\n');
    
    for (const line of lines) {
      if (line.trim()) {
        phaseCount++;
        res.write(`data: ${JSON.stringify({
          type: 'phase',
          phase: phaseCount,
          content: line
        })}\n\n`);
      }
    }
  });
  
  pythonProcess.stderr.on('data', (data) => {
    console.error(`[Python stderr]: ${data}`);
    res.write(`data: ${JSON.stringify({
      type: 'error',
      message: data.toString()
    })}\n\n`);
  });
  
  pythonProcess.on('close', (code) => {
    if (code === 0) {
      // Read results JSON if created
      const resultsFile = path.join(__dirname, 'pantheon_results.json');
      let results = null;
      
      try {
        if (fs.existsSync(resultsFile)) {
          results = JSON.parse(fs.readFileSync(resultsFile, 'utf8'));
        }
      } catch (e) {
        console.error('Could not read results:', e);
      }
      
      res.write(`data: ${JSON.stringify({
        type: 'complete',
        message: '✅ Pantheon ritual complete',
        results: results
      })}\n\n`);
    } else {
      res.write(`data: ${JSON.stringify({
        type: 'error',
        message: `Python process exited with code ${code}`
      })}\n\n`);
    }
    
    res.end();
  });
  
  // Handle client disconnect
  req.on('close', () => {
    pythonProcess.kill();
  });
});

/**
 * GET /api/status
 * Check if API key is configured
 */
app.get('/api/status', (req, res) => {
  res.json({
    configured: !!config.apiKey,
    provider: config.apiProvider || 'none'
  });
});

/**
 * GET /api/results
 * Get latest pantheon results
 */
app.get('/api/results', (req, res) => {
  const resultsFile = path.join(__dirname, 'pantheon_results.json');
  
  try {
    if (fs.existsSync(resultsFile)) {
      const results = JSON.parse(fs.readFileSync(resultsFile, 'utf8'));
      return res.json(results);
    }
  } catch (e) {
    console.error('Error reading results:', e);
  }
  
  res.status(404).json({ error: 'No results yet' });
});

// === START SERVER ===
app.listen(PORT, () => {
  console.log(`\n🔥⚡ Vibe Coder Pantheon API Server`);
  console.log(`📍 Running on http://localhost:${PORT}`);
  console.log(`\n   1. Open browser: http://localhost:${PORT}`);
  console.log(`   2. Enter your API key (OpenAI or Claude)`);
  console.log(`   3. Describe your vibe`);
  console.log(`   4. Watch the Pantheon work in real-time\n`);
});
