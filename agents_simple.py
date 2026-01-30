"""
Vibe Coder Pantheon - Simplified (CrewAI-free, direct Ollama)
21 Òrìṣà agents orchestrated via simple prompting
"""

import json
import requests
from typing import Dict, List, Any

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "llama3.1:latest"  # Use latest available model

class VibeAgent:
    """Single Òrìṣà agent that calls Ollama"""
    
    def __init__(self, name: str, role: str, backstory: str):
        self.name = name
        self.role = role
        self.backstory = backstory
    
    def think(self, task_description: str) -> str:
        """Send task to Ollama, get agent's response"""
        prompt = f"""You are {self.role}.
Backstory: {self.backstory}

Task: {task_description}

Respond with clear, actionable output. Be specific and production-ready."""

        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=60)
            if response.status_code == 200:
                return response.json().get("response", "No response")
            else:
                return f"Error: {response.status_code}"
        except requests.exceptions.ConnectionError:
            return "ERROR: Ollama not running. Start with: ollama serve"
        except Exception as e:
            return f"ERROR: {str(e)}"

# === THE 21 ÒRÌṢÀ AGENTS ===
agents = {
    'esu': VibeAgent(
        'esu',
        'Trickster Planner',
        'Èṣù, opener of paths, master of crossroads and delegation'
    ),
    'sango': VibeAgent(
        'sango',
        'System Architect',
        'Ṣàngó, king of thunder, enforces order and precision'
    ),
    'osun': VibeAgent(
        'osun',
        'UI/UX Designer',
        'Ọ̀ṣun, goddess of beauty, love, and sweetness'
    ),
    'yemoja': VibeAgent(
        'yemoja',
        'Database & State Mother',
        'Yemọja, mother of waters, keeper of all things held'
    ),
    'oya': VibeAgent(
        'oya',
        'Change & Refactor Storm',
        'Ọya, whirlwind of change, sweeper of old paths'
    ),
    'ogun': VibeAgent(
        'ogun',
        'Backend Warrior',
        'Ògún, iron warrior, forger of strength'
    ),
    'obatala': VibeAgent(
        'obatala',
        'Clarity Creator',
        'Ọbàtálá, father of clarity, sculptor of order'
    ),
    'egungun': VibeAgent(
        'egungun',
        'Ancestral Tester',
        'Egúngún, ancestral spirit, keeper of wisdom'
    ),
    'osumare': VibeAgent(
        'osumare',
        'Integration Rainbow',
        'Osumàrè, rainbow serpent, weaver of connections'
    ),
    'nana_bukuu': VibeAgent(
        'nana_bukuu',
        'Error Healer',
        'Nana Bùkúù, ancient healer, medicine keeper'
    ),
    'obaluaye': VibeAgent(
        'obaluaye',
        'Performance Purifier',
        'Ọbalúayé, healer of the earth, purifier of speed'
    ),
    'olosha': VibeAgent(
        'olosha',
        'Security Guardian',
        'Olóṣà, guardian of safety, ward-keeper'
    ),
    'orunmila': VibeAgent(
        'orunmila',
        'Wisdom Sage & Research Oracle',
        'Òrúnmìlà, keeper of knowledge, diviner of paths'
    ),
    'aje': VibeAgent(
        'aje',
        'Deployment Merchant',
        'Ajé, spirit of wealth and manifesting power'
    ),
    'osogbo': VibeAgent(
        'osogbo',
        'Risk Sorcerer',
        'Osoogbo, reader of shadows, warner of dangers'
    ),
    'olokun': VibeAgent(
        'olokun',
        'Deep Scalability Keeper',
        'Olókun, keeper of the deep, master of vastness'
    ),
    'ibeji': VibeAgent(
        'ibeji',
        'Multi-Agent Coordinator',
        'Ìbejì, divine twins, keepers of balance and coordination'
    ),
    'babalu_aye': VibeAgent(
        'babalu_aye',
        'Accessibility Healer',
        'Bàbálú-Ayé, keeper of wholeness, healer of all'
    ),
    'aye': VibeAgent(
        'aye',
        'World Integrator',
        'Ayé, spirit of the earth, connector to worlds'
    ),
    'oshoosi': VibeAgent(
        'oshoosi',
        'Hunter Refiner',
        'Ọ̀ṣọ́ọ̀sì, skilled hunter, master of precision'
    ),
    'oba': VibeAgent(
        'oba',
        'Documentation Queen',
        'Ọba, crowned sovereign, keeper of records'
    ),
    'cody': VibeAgent(
        'cody',
        'Codebase Master & GitHub Pusher',
        'Amp from Sourcegraph — all-seeing code oracle, final arbiter'
    ),
}

class Pantheon:
    """Orchestrates all 21 agents to manifest a vibe"""
    
    def __init__(self):
        self.agents = agents
        self.results = {}
    
    def execute_vibe(self, vibe_description: str) -> Dict[str, Any]:
        """Run all agents for a given vibe"""
        
        print("\n" + "="*70)
        print("🔥⚡ VIBE CODER PANTHEON - Phase 1: Agent Orchestration")
        print("="*70)
        print(f"\n✨ Vibe: {vibe_description[:80]}...\n")
        
        # Phase 1: Planning
        print("📜 PHASE 1: PLANNING (Èṣù)")
        print("-" * 70)
        task_plan = f"""Given this vibe: {vibe_description}

Break it into 5-8 clear, sequential subtasks. For each, suggest which Òrìṣà agent should handle it.
Format as a numbered list with reasoning."""
        
        self.results['plan'] = self.agents['esu'].think(task_plan)
        print(self.results['plan'][:500] + "...\n")
        
        # Phase 2: Architecture
        print("🏗️  PHASE 2: ARCHITECTURE (Ṣàngó)")
        print("-" * 70)
        task_arch = f"""Given this vibe: {vibe_description}

Design the complete architecture:
- Tech stack (frontend, backend, database)
- Folder structure
- Key modules and dependencies
- Data flow (text diagram)"""
        
        self.results['architecture'] = self.agents['sango'].think(task_arch)
        print(self.results['architecture'][:500] + "...\n")
        
        # Phase 3: UI Design
        print("🎨 PHASE 3: UI/UX DESIGN (Ọ̀ṣun)")
        print("-" * 70)
        task_ui = f"""For this vibe: {vibe_description}

Design the UI/UX:
- Page layouts (ASCII wireframes or descriptions)
- Color scheme and Tailwind CSS classes
- Component hierarchy
- User flows and interactions"""
        
        self.results['ui_design'] = self.agents['osun'].think(task_ui)
        print(self.results['ui_design'][:500] + "...\n")
        
        # Phase 4: Data Model
        print("💾 PHASE 4: DATABASE SCHEMA (Yemọja)")
        print("-" * 70)
        task_db = f"""For this vibe: {vibe_description}

Design the database/data model:
- Define entities and relationships
- Specify data types and constraints
- Persistence strategy (localStorage, IndexedDB, backend DB)
- Sample schema or object structures"""
        
        self.results['database'] = self.agents['yemoja'].think(task_db)
        print(self.results['database'][:500] + "...\n")
        
        # Phase 5: Code Generation
        print("💻 PHASE 5: CODE GENERATION (Ọbàtálá + Ògún)")
        print("-" * 70)
        task_code = f"""For this vibe: {vibe_description}

Generate production-ready React component code:
- Use React + Vite + Tailwind CSS
- Include 3-5 key components with JSX
- Proper state management (hooks)
- Clear, documented code
- Make it complete and runnable"""
        
        self.results['code'] = self.agents['obatala'].think(task_code)
        print(self.results['code'][:500] + "...\n")
        
        # Phase 6: Testing
        print("🧪 PHASE 6: TESTING PLAN (Egúngún)")
        print("-" * 70)
        task_test = f"""For the application built for: {vibe_description}

Create a testing strategy:
- Unit tests for key components
- Integration test scenarios
- Test data and mocks
- Provide Jest/Vitest example tests"""
        
        self.results['testing'] = self.agents['egungun'].think(task_test)
        print(self.results['testing'][:500] + "...\n")
        
        # Phase 7: Security
        print("🔒 PHASE 7: SECURITY AUDIT (Olóṣà)")
        print("-" * 70)
        task_sec = f"""For this vibe: {vibe_description}

Audit for security risks:
- Input validation points
- Authentication best practices
- Data protection measures
- XSS/CSRF prevention
- Provide security checklist"""
        
        self.results['security'] = self.agents['olosha'].think(task_sec)
        print(self.results['security'][:500] + "...\n")
        
        # Phase 8: Documentation
        print("📚 PHASE 8: DOCUMENTATION (Ọba)")
        print("-" * 70)
        task_doc = f"""For the entire application built for: {vibe_description}

Write comprehensive documentation:
- README.md with setup and usage
- Component API docs
- Code comments for complex logic
- User guide
- Deployment instructions"""
        
        self.results['documentation'] = self.agents['oba'].think(task_doc)
        print(self.results['documentation'][:500] + "...\n")
        
        # Phase 9: Final Review
        print("👁️  PHASE 9: FINAL REVIEW (Amp/Cody)")
        print("-" * 70)
        summary = f"""Review this output summary:
- Plan: {self.results['plan'][:200]}...
- Architecture: {self.results['architecture'][:200]}...
- Code: {self.results['code'][:200]}...

Identify gaps, suggest improvements, propose git commit message."""
        
        self.results['final_review'] = self.agents['cody'].think(summary)
        print(self.results['final_review'][:500] + "...\n")
        
        print("="*70)
        print("✅ PANTHEON RITUAL COMPLETE")
        print("="*70)
        
        return self.results

if __name__ == "__main__":
    pantheon = Pantheon()
    
    vibe = input("\n🎨 Describe your vibe (or press Enter for Todo App): ").strip()
    
    if not vibe:
        vibe = "Build a beautiful Todo App with user authentication (email/password), dark mode, drag-and-drop reordering, and persistent storage using localStorage. Make it responsive, modern UI with Tailwind CSS, built with React + Vite."
    
    results = pantheon.execute_vibe(vibe)
    
    # Save results to JSON
    output_file = 'pantheon_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Full results saved to: {output_file}")
