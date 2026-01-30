#!/usr/bin/env python3
"""
Test Pantheon with auto-input (no interactive prompt)
"""
from agents_simple import Pantheon

if __name__ == "__main__":
    pantheon = Pantheon()
    
    vibe = "Build a beautiful Todo App with user authentication (email/password), dark mode, drag-and-drop reordering, and persistent storage using localStorage. Make it responsive, modern UI with Tailwind CSS, built with React + Vite."
    
    results = pantheon.execute_vibe(vibe)
    
    # Save results
    import json
    with open('pantheon_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Results saved to pantheon_results.json")
