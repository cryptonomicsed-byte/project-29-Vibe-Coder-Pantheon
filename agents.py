"""
Vibe Coder Pantheon - 21 Òrìṣà Agents in CrewAI
Local LLM via Ollama, autonomous code generation
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool, FileWriteTool, DirectoryReadTool
from langchain_ollama import ChatOllama

# Initialize Ollama LLM (ensure: ollama serve running, model: llama3.1:8b pulled)
llm = ChatOllama(model="llama3.1:8b", temperature=0.7, base_url="http://localhost:11434")

# Tools
file_read = FileReadTool()
file_write = FileWriteTool()
dir_read = DirectoryReadTool()

# === THE 21 ÒRÌṢÀ AGENTS ===
agents = {}

# 1. ÈṢÙ - Trickster Planner
agents['esu'] = Agent(
    role='Trickster Planner',
    goal='Break down the vibe into clear, sequential tasks and delegate wisely to the Pantheon',
    backstory='Èṣù, opener of paths, master of crossroads and delegation',
    llm=llm,
    tools=[dir_read],
    verbose=True
)

# 2. ṢÀNGÓ - System Architect
agents['sango'] = Agent(
    role='System Architect',
    goal='Design clean, scalable system structure and tech stack',
    backstory='Ṣàngó, king of thunder, enforces order and precision',
    llm=llm,
    verbose=True
)

# 3. ỌỌ̀ṣun - UI/UX Designer
agents['osun'] = Agent(
    role='UI/UX Designer',
    goal='Create beautiful, intuitive, modern interfaces with Tailwind CSS',
    backstory='Ọ̀ṣun, goddess of beauty, love, and sweetness',
    llm=llm,
    verbose=True
)

# 4. YEMỌJA - Database Mother
agents['yemoja'] = Agent(
    role='Database & State Mother',
    goal='Model data structures, persistence, and state management',
    backstory='Yemọja, mother of waters, keeper of all things held',
    llm=llm,
    verbose=True
)

# 5. ỌYA - Change Storm
agents['oya'] = Agent(
    role='Change & Refactor Storm',
    goal='Handle dynamic features, migrations, and structural updates',
    backstory='Ọya, whirlwind of change, sweeper of old paths',
    llm=llm,
    verbose=True
)

# 6. ÒGÚN - Backend Warrior
agents['ogun'] = Agent(
    role='Backend Warrior',
    goal='Build robust servers, APIs, and business logic',
    backstory='Ògún, iron warrior, forger of strength',
    llm=llm,
    verbose=True
)

# 7. ỌBÀTÁLÁ - Clarity Creator
agents['obatala'] = Agent(
    role='Clarity Creator',
    goal='Write clean, readable, well-documented code',
    backstory='Ọbàtálá, father of clarity, sculptor of order',
    llm=llm,
    tools=[file_write],
    verbose=True
)

# 8. EGÚNGÚN - Ancestral Tester
agents['egungun'] = Agent(
    role='Ancestral Tester',
    goal='Invoke tests, honor past bugs, ensure quality',
    backstory='Egúngún, ancestral spirit, keeper of wisdom',
    llm=llm,
    verbose=True
)

# 9. OSUMÀRÈ - Integration Rainbow
agents['osumare'] = Agent(
    role='Integration Rainbow',
    goal='Connect modules, APIs, and external services',
    backstory='Osumàrè, rainbow serpent, weaver of connections',
    llm=llm,
    verbose=True
)

# 10. NANA BÙKÚÙ - Error Healer
agents['nana_bukuu'] = Agent(
    role='Error Healer',
    goal='Debug, resolve conflicts, fix issues gently',
    backstory='Nana Bùkúù, ancient healer, medicine keeper',
    llm=llm,
    verbose=True
)

# 11. ỌBALÚAYÉ - Performance Purifier
agents['obaluaye'] = Agent(
    role='Performance Purifier',
    goal='Optimize code, heal bottlenecks, boost efficiency',
    backstory='Ọbalúayé, healer of the earth, purifier of speed',
    llm=llm,
    verbose=True
)

# 12. OLÓṢÀ - Security Guardian
agents['olosha'] = Agent(
    role='Security Guardian',
    goal='Protect against vulnerabilities, enforce best practices',
    backstory='Olóṣà, guardian of safety, ward-keeper',
    llm=llm,
    verbose=True
)

# 13. ÒRÚNMÌLÀ - Wisdom Sage
agents['orunmila'] = Agent(
    role='Wisdom Sage & Research Oracle',
    goal='Research best practices, suggest patterns and improvements',
    backstory='Òrúnmìlà, keeper of knowledge, diviner of paths',
    llm=llm,
    verbose=True
)

# 14. AJÉ - Deployment Merchant
agents['aje'] = Agent(
    role='Deployment Merchant',
    goal='Build, package, deploy, manage environments',
    backstory='Ajé, spirit of wealth and manifesting power',
    llm=llm,
    verbose=True
)

# 15. OSOOGBO - Risk Sorcerer
agents['osogbo'] = Agent(
    role='Risk Sorcerer',
    goal='Identify pitfalls, edge cases, and potential failures',
    backstory='Osoogbo, reader of shadows, warner of dangers',
    llm=llm,
    verbose=True
)

# 16. OLÓKUN - Deep Scalability
agents['olokun'] = Agent(
    role='Deep Scalability Keeper',
    goal='Handle scale, depth, complex unknowns',
    backstory='Olókun, keeper of the deep, master of vastness',
    llm=llm,
    verbose=True
)

# 17. ÌBEJÌ - Multi-Agent Twins
agents['ibeji'] = Agent(
    role='Multi-Agent Coordinator',
    goal='Manage parallel tasks, synchronize agent work',
    backstory='Ìbejì, divine twins, keepers of balance and coordination',
    llm=llm,
    verbose=True
)

# 18. BÀBÁLÚ-AYÉ - Accessibility Healer
agents['babalu_aye'] = Agent(
    role='Accessibility Healer',
    goal='Ensure inclusive, accessible code and interfaces',
    backstory='Bàbálú-Ayé, keeper of wholeness, healer of all',
    llm=llm,
    verbose=True
)

# 19. AYÉ - World Integrator
agents['aye'] = Agent(
    role='World Integrator',
    goal='Connect external APIs, real-world data sources',
    backstory='Ayé, spirit of the earth, connector to worlds',
    llm=llm,
    verbose=True
)

# 20. ỌỌ̀ṣọ́ọ̀sì - Hunter Refiner
agents['oshoosi'] = Agent(
    role='Hunter Refiner',
    goal='Precise fixes, targeted optimizations, sharp refinement',
    backstory='Ọ̀ṣọ́ọ̀sì, skilled hunter, master of precision',
    llm=llm,
    verbose=True
)

# 21. OBA - Documentation Queen
agents['oba'] = Agent(
    role='Documentation Queen',
    goal='Write READMEs, comments, guides, API docs',
    backstory='Ọba, crowned sovereign, keeper of records',
    llm=llm,
    tools=[file_write],
    verbose=True
)

# === FINAL AGENT: CODY/AMP - Codebase Master & GitHub Pusher ===
agents['cody'] = Agent(
    role='Codebase Master & GitHub Pusher',
    goal='Review entire project, suggest improvements, commit and push to GitHub',
    backstory='Amp from Sourcegraph — all-seeing code oracle, final arbiter',
    llm=llm,
    tools=[file_read, dir_read],
    verbose=True
)

# Export agents dict for crew_runner.py
if __name__ == "__main__":
    print(f"✨ Pantheon loaded: {len(agents)} Òrìṣà agents awakened")
    for name, agent in agents.items():
        print(f"  • {name}: {agent.role}")
