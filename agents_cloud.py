"""
Vibe Coder Pantheon - Multi-LLM Version
21 Òrìṣà agents orchestrated via multiple LLM providers
Works with: OpenAI, Claude, Gemini, Mistral, Groq, Perplexity, Ollama, Cohere
"""

import json
import os
from typing import Dict, Any
from dotenv import load_dotenv
from llm_providers import get_provider

load_dotenv()

class VibeAgent:
    """Òrìṣà agent that supports multiple LLM backends"""
    
    def __init__(self, name: str, role: str, backstory: str):
        self.name = name
        self.role = role
        self.backstory = backstory
        self.provider = None
        self.api_key = None
    
    def set_provider(self, provider_name: str, api_key: str, **kwargs):
        """Set the LLM provider for this agent"""
        self.provider_name = provider_name
        self.api_key = api_key
        try:
            self.provider = get_provider(provider_name, api_key, **kwargs)
        except Exception as e:
            print(f"Error initializing {provider_name}: {str(e)}")
            self.provider = None
    
    def think(self, task_description: str) -> str:
        """Send task to configured LLM"""
        prompt = f"""You are {self.role}.
Backstory: {self.backstory}

Task: {task_description}

Respond with clear, actionable output. Be specific and production-ready."""

        if self.provider:
            return self.provider.generate(prompt)
        
        # Fallback to mock response
        return self._mock_response(task_description)
    
    def _mock_response(self, task_description: str) -> str:
        """Mock response for demo (when no API keys set)"""
        mocks = {
            "planning": "1. Setup authentication system\n2. Design database schema\n3. Create React components\n4. Build API endpoints\n5. Add dark mode\n6. Implement drag-and-drop\n7. Write tests\n8. Deploy",
            "architecture": "Frontend: React + Vite + Tailwind\nBackend: Node.js + Express\nDatabase: PostgreSQL\nAuth: JWT\nStorage: Redis (sessions)",
            "ui": "Header with dark mode toggle, Auth modal, Todo list with cards, Drag-and-drop zone, Footer",
            "database": "users (id, email, password_hash, created_at)\ntodos (id, user_id, title, completed, order, created_at)",
            "code": "function TodoApp() {\n  const [todos, setTodos] = useState([]);\n  return <div className='p-4'>TODO LIST</div>;\n}",
            "testing": "Unit tests for auth, Integration tests for CRUD, E2E tests for user flow",
            "security": "Hash passwords with bcrypt, Validate inputs, Use HTTPS, Implement CORS properly",
            "documentation": "README with setup, API docs, Component docs, User guide",
            "review": "Good architecture. Add error boundaries, improve accessibility, add logging."
        }
        
        for key, response in mocks.items():
            if key in task_description.lower():
                return response
        
        return "Agent thinking... [mock response]"

# === THE 21 ÒRÌṢÀ AGENTS ===
agents = {
    'esu': VibeAgent('esu', 'Trickster Planner', 'Èṣù, opener of paths'),
    'sango': VibeAgent('sango', 'System Architect', 'Ṣàngó, king of thunder'),
    'osun': VibeAgent('osun', 'UI/UX Designer', 'Ọ̀ṣun, goddess of beauty'),
    'yemoja': VibeAgent('yemoja', 'Database Mother', 'Yemọja, mother of waters'),
    'oya': VibeAgent('oya', 'Change Storm', 'Ọya, whirlwind of change'),
    'ogun': VibeAgent('ogun', 'Backend Warrior', 'Ògún, iron warrior'),
    'obatala': VibeAgent('obatala', 'Clarity Creator', 'Ọbàtálá, father of clarity'),
    'egungun': VibeAgent('egungun', 'Ancestral Tester', 'Egúngún, ancestral spirit'),
    'osumare': VibeAgent('osumare', 'Integration Rainbow', 'Osumàrè, rainbow serpent'),
    'nana_bukuu': VibeAgent('nana_bukuu', 'Error Healer', 'Nana Bùkúù, ancient healer'),
    'obaluaye': VibeAgent('obaluaye', 'Performance Purifier', 'Ọbalúayé, healer'),
    'olosha': VibeAgent('olosha', 'Security Guardian', 'Olóṣà, guardian'),
    'orunmila': VibeAgent('orunmila', 'Wisdom Sage', 'Òrúnmìlà, keeper'),
    'aje': VibeAgent('aje', 'Deployment Merchant', 'Ajé, spirit of wealth'),
    'osogbo': VibeAgent('osogbo', 'Risk Sorcerer', 'Osoogbo, reader'),
    'olokun': VibeAgent('olokun', 'Deep Scalability', 'Olókun, keeper'),
    'ibeji': VibeAgent('ibeji', 'Multi-Agent Coordinator', 'Ìbejì, divine twins'),
    'babalu_aye': VibeAgent('babalu_aye', 'Accessibility Healer', 'Bàbálú-Ayé'),
    'aye': VibeAgent('aye', 'World Integrator', 'Ayé, spirit of earth'),
    'oshoosi': VibeAgent('oshoosi', 'Hunter Refiner', 'Ọ̀ṣọ́ọ̀sì, hunter'),
    'oba': VibeAgent('oba', 'Documentation Queen', 'Ọba, crowned sovereign'),
    'cody': VibeAgent('cody', 'Codebase Master', 'Amp from Sourcegraph'),
}

class Pantheon:
    """Orchestrates 21 agents with configurable LLM provider"""
    
    def __init__(self, provider_name: str = None, api_key: str = None, **provider_kwargs):
        self.agents = agents
        self.results = {}
        
        # Set provider for all agents
        if provider_name and api_key:
            self.set_provider(provider_name, api_key, **provider_kwargs)
    
    def set_provider(self, provider_name: str, api_key: str, **kwargs):
        """Set LLM provider for all agents"""
        for agent in self.agents.values():
            agent.set_provider(provider_name, api_key, **kwargs)
    
    def execute_vibe(self, vibe_description: str) -> Dict[str, Any]:
        """Run all agents for a vibe"""
        
        print("\n" + "="*70)
        print("🔥⚡ VIBE CODER PANTHEON - Phase 1")
        print("="*70)
        print(f"\n✨ Vibe: {vibe_description[:70]}...\n")
        
        phases = [
            ('plan', 'Èṣù', 'PLANNING', "Break into 5-8 clear, sequential subtasks"),
            ('arch', 'Ṣàngó', 'ARCHITECTURE', "Design system structure and tech stack"),
            ('ui', 'Ọ̀ṣun', 'UI/UX', "Design pages, colors, and components"),
            ('db', 'Yemọja', 'DATABASE', "Design data models and schema"),
            ('code', 'Ọbàtálá', 'CODE', "Generate React component code"),
            ('test', 'Egúngún', 'TESTING', "Create test suite strategy"),
            ('sec', 'Olóṣà', 'SECURITY', "Audit for vulnerabilities"),
            ('doc', 'Ọba', 'DOCUMENTATION', "Write README and guides"),
            ('review', 'Amp', 'FINAL REVIEW', "Review and commit plan"),
        ]
        
        for phase_id, agent_name, phase_label, task_desc in phases:
            print(f"{'⚡' if phase_id == 'plan' else '📋'} PHASE: {phase_label} ({agent_name})")
            print("-" * 70)
            
            agent = self.agents.get(agent_name.lower().replace(' ', '_').replace('ṣà', 'sango').replace('ọ', 'o').replace('è', 'e'))
            if not agent:
                agent = self.agents['esu']
            
            full_task = f"{task_desc}\n\nVibe: {vibe_description}"
            response = agent.think(full_task)
            
            self.results[phase_id] = response
            print(response[:300] + "...\n")
        
        print("="*70)
        print("✅ PANTHEON COMPLETE")
        print("="*70)
        
        return self.results

if __name__ == "__main__":
    pantheon = Pantheon()
    
    vibe = input("🎨 Vibe (or Enter for Todo App): ").strip()
    if not vibe:
        vibe = "Todo app with auth, dark mode, drag-and-drop, React + Tailwind"
    
    results = pantheon.execute_vibe(vibe)
    
    with open('pantheon_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Results saved to pantheon_results.json")
