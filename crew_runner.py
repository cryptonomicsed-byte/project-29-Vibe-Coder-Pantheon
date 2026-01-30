"""
Vibe Coder Pantheon - CrewAI Crew Executor
Orchestrates 21 agents to manifest your vibe into reality
"""

from crewai import Task, Crew, Process
from agents import agents

def create_pantheon_crew(vibe_description: str):
    """
    Create and run the Pantheon crew for a given vibe
    """
    
    # === TASK DEFINITIONS ===
    
    task_plan = Task(
        description=f"""Analyze this vibe and create a detailed, numbered task breakdown:
        
VIBE: {vibe_description}

Break it into 5-10 clear, sequential subtasks. Assign each task to an appropriate Òrìṣà agent.
Format: 
1. [Task Name] → Assigned to: [Agent] | Reason: [Why this agent]
2. [Task Name] → Assigned to: [Agent] | Reason: [Why this agent]
...""",
        agent=agents['esu'],
        expected_output="Numbered task list with agent assignments and reasoning"
    )
    
    task_architect = Task(
        description=f"""Given this vibe: {vibe_description}

Design the complete architecture:
- Tech stack (frontend, backend, database, etc.)
- Folder structure
- Key modules and how they connect
- Data flow diagram (text-based)

Be specific and production-ready.""",
        agent=agents['sango'],
        expected_output="Architecture document with tech stack, folder structure, and data flow"
    )
    
    task_ui_design = Task(
        description=f"""For this vibe: {vibe_description}

Design the UI/UX:
- Page layouts (wireframes as ASCII art or descriptions)
- Color scheme and styling (Tailwind CSS classes)
- Component hierarchy
- User flow and interactions
- Responsive design notes

Create beautiful, intuitive design specs.""",
        agent=agents['osun'],
        expected_output="Complete UI/UX design document with layouts and component specs"
    )
    
    task_database = Task(
        description=f"""For this vibe: {vibe_description}

Design the database schema:
- Define all entities and relationships
- Specify data types and constraints
- Plan for persistence (localStorage, IndexedDB, or backend DB)
- Consider future scaling

Provide SQL/schema pseudo-code if backend, or JS object structures if frontend-only.""",
        agent=agents['yemoja'],
        expected_output="Complete database schema and data model design"
    )
    
    task_backend = Task(
        description=f"""For this vibe: {vibe_description}

Design and specify the backend logic (if needed):
- API endpoints (REST or GraphQL)
- Authentication/authorization flow
- Business logic and algorithms
- Error handling strategy

Provide endpoint definitions with methods, paths, and payloads.""",
        agent=agents['ogun'],
        expected_output="API specification and backend logic design"
    )
    
    task_frontend_code = Task(
        description=f"""For this vibe: {vibe_description}

Generate the frontend code structure:
- React component hierarchy (using Vite + React)
- Component files and their responsibilities
- State management approach
- Styling with Tailwind CSS

Provide a complete, working React component structure.""",
        agent=agents['obatala'],
        expected_output="Complete React component code with Tailwind styling"
    )
    
    task_testing = Task(
        description=f"""For the application built for: {vibe_description}

Create a comprehensive testing strategy:
- Unit tests for components and logic
- Integration test scenarios
- E2E test cases
- Test data and mocks

Provide test code (Jest/Vitest examples).""",
        agent=agents['egungun'],
        expected_output="Complete testing plan and test code examples"
    )
    
    task_security = Task(
        description=f"""For this vibe: {vibe_description}

Audit for security risks:
- Input validation and sanitization
- Authentication best practices
- Data protection measures
- API security (if backend)
- Client-side security

Provide security recommendations and code patches.""",
        agent=agents['olosha'],
        expected_output="Security audit report with recommendations and fixes"
    )
    
    task_optimization = Task(
        description=f"""For the application built for: {vibe_description}

Identify performance optimizations:
- Code splitting and lazy loading
- Bundle size reduction
- Caching strategies
- Database query optimization
- Rendering performance (React)

Provide specific optimizations and their impact.""",
        agent=agents['obaluaye'],
        expected_output="Performance optimization plan with specific improvements"
    )
    
    task_documentation = Task(
        description=f"""For the entire application built for: {vibe_description}

Write comprehensive documentation:
- README.md with setup instructions
- Component API documentation
- Code comments for complex logic
- Deployment guide
- User guide/manual

Make it clear and beginner-friendly.""",
        agent=agents['oba'],
        expected_output="Complete documentation including README, API docs, and guides"
    )
    
    task_final_review = Task(
        description=f"""Review the entire application output for the vibe: {vibe_description}

As the final arbiter:
1. Check all code for quality, correctness, and consistency
2. Identify any gaps or missing features
3. Suggest architectural improvements
4. Propose a git commit message and GitHub push strategy
5. Flag any critical issues

Prepare a final report and commit plan.""",
        agent=agents['cody'],
        expected_output="Final review report, suggested improvements, and commit plan"
    )
    
    # === CREATE CREW ===
    tasks = [
        task_plan,
        task_architect,
        task_ui_design,
        task_database,
        task_backend,
        task_frontend_code,
        task_testing,
        task_security,
        task_optimization,
        task_documentation,
        task_final_review
    ]
    
    pantheon_crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.hierarchical,
        manager_agent=agents['esu'],  # Èṣù orchestrates
        verbose=2
    )
    
    return pantheon_crew

def main():
    print("\n" + "="*70)
    print("🔥⚡ VIBE CODER PANTHEON - Phase 1: Agent Orchestration")
    print("="*70)
    print("\n📜 21 Òrìṣà Agents awakened. Awaiting your vibe...\n")
    
    vibe = input("🎨 Describe your vibe (or press Enter for Todo App): ").strip()
    
    if not vibe:
        vibe = "Build a beautiful Todo App with user authentication (email/password), dark mode, drag-and-drop reordering, and persistent storage using localStorage. Make it responsive, modern UI with Tailwind CSS, built with React + Vite."
    
    print(f"\n✨ Vibe received: {vibe[:80]}...\n")
    print("🔮 Pantheon begins summoning...\n")
    
    crew = create_pantheon_crew(vibe)
    result = crew.kickoff()
    
    print("\n" + "="*70)
    print("✅ PANTHEON RITUAL COMPLETE")
    print("="*70)
    print("\n📜 FINAL OUTPUT:\n")
    print(result)
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
