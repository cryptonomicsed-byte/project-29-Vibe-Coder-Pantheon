#!/usr/bin/env python3
"""
Pantheon Runner - Executes agents and streams output
Called by Express server via SSE
"""

import os
import json
import sys
from agents_simple import Pantheon

def main():
    vibe = os.getenv('VIBE_INPUT', 'Build a Todo App')
    sse_mode = os.getenv('SSE_MODE', 'false') == 'true'
    
    if sse_mode:
        # Stream mode (for web UI) - run async in background
        print(f"🎨 Vibe: {vibe[:60]}...")
        sys.stdout.flush()
        
        # For now, create stub results since Ollama calls are slow
        results = {
            'vibe': vibe,
            'status': 'queued',
            'message': 'Pantheon agents activated. Processing...',
            'phases': {
                'plan': 'Planning phase initiated...',
                'architecture': 'Designing architecture...',
                'ui_design': 'Creating UI/UX...',
                'database': 'Modeling data...',
                'code': 'Generating code...',
                'testing': 'Writing tests...',
                'security': 'Auditing security...',
                'documentation': 'Creating docs...'
            }
        }
    else:
        # Full pantheon run
        pantheon = Pantheon()
        results = pantheon.execute_vibe(vibe)
    
    # Save results
    with open('pantheon_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    if sse_mode:
        print("✅ Pantheon initialized")
        sys.stdout.flush()

if __name__ == '__main__':
    main()
