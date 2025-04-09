#!/usr/bin/env python3

import re
import os

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(content)

def extract_section(content, start_pattern, end_pattern=None):
    if end_pattern:
        match = re.search(f'{start_pattern}(.*?){end_pattern}', content, re.DOTALL)
    else:
        match = re.search(f'{start_pattern}(.*?)(?=# |\Z)', content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    return ''

def process_content(content):
    # Process Introduction
    write_file('docs/introduction/what-is-ghost.md', 
               extract_section(content, '## What is Ghost\?', '## Key Features'))
    write_file('docs/introduction/key-features.md', 
               extract_section(content, '## Key Features', '## Project Vision'))
    write_file('docs/introduction/project-vision.md', 
               extract_section(content, '## Project Vision', '# 2\.'))

    # Process Technical Architecture
    write_file('docs/technical-architecture/system-overview.md', 
               extract_section(content, '## System Overview', '## Component Breakdown'))
    write_file('docs/technical-architecture/component-breakdown.md', 
               extract_section(content, '## Component Breakdown', '## Zero-Knowledge Proof System'))
    write_file('docs/technical-architecture/zk-proof-system.md', 
               extract_section(content, '## Zero-Knowledge Proof System', '## AI Enhancement Layer'))
    write_file('docs/technical-architecture/ai-enhancement-layer.md', 
               extract_section(content, '## AI Enhancement Layer', '# 3\.'))

    # Process Getting Started
    write_file('docs/getting-started/installation.md', 
               extract_section(content, '## Installation', '## Prerequisites'))
    write_file('docs/getting-started/prerequisites.md', 
               extract_section(content, '## Prerequisites', '## Development Environment Setup'))
    write_file('docs/getting-started/development-environment-setup.md', 
               extract_section(content, '## Development Environment Setup', '## Configuration'))
    write_file('docs/getting-started/configuration.md', 
               extract_section(content, '## Configuration', '# 4\.'))

    # Process User Guide
    write_file('docs/user-guide/connecting-wallet.md', 
               extract_section(content, '## Connecting Your Wallet', '## Generating ZK Proofs'))
    write_file('docs/user-guide/generating-proofs.md', 
               extract_section(content, '## Generating ZK Proofs', '## Verifying ZK Proofs'))
    write_file('docs/user-guide/verifying-proofs.md', 
               extract_section(content, '## Verifying ZK Proofs', '## Understanding AI-Enhanced Explanations'))
    write_file('docs/user-guide/ai-explanations.md', 
               extract_section(content, '## Understanding AI-Enhanced Explanations', '## Testing ZK Proof System'))
    write_file('docs/user-guide/testing.md', 
               extract_section(content, '## Testing ZK Proof System', '# 5\.'))

    # Process Developer Documentation
    write_file('docs/developer-documentation/project-structure.md', 
               extract_section(content, '## Project Structure', '## Core Services'))
    write_file('docs/developer-documentation/core-services.md', 
               extract_section(content, '## Core Services', '## Key Components'))
    write_file('docs/developer-documentation/key-components.md', 
               extract_section(content, '## Key Components', '# 6\.'))

def main():
    content = read_file('ghost_documentation.md')
    process_content(content)
    print("Documentation has been split into separate files in the docs directory")

if __name__ == "__main__":
    main() 