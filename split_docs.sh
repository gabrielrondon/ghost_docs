#!/bin/bash

# Function to create directory and parent README
create_section() {
    local dir=$1
    local title=$2
    mkdir -p "docs/$dir"
    echo "# $title\n\nThis section covers $title related topics.\n" > "docs/$dir/README.md"
}

# Create main sections and their subdirectories
create_section "introduction" "Introduction"
create_section "technical-architecture" "Technical Architecture"
create_section "getting-started" "Getting Started"
create_section "user-guide" "User Guide"
create_section "developer-documentation" "Developer Documentation"
create_section "zk-proof-canister" "ZK Proof Canister"
create_section "ai-components" "AI Components"
create_section "security" "Security Considerations"
create_section "roadmap" "Future Roadmap"
create_section "api-reference" "API Reference"
create_section "troubleshooting" "Troubleshooting"
create_section "contributing" "Contributing"
create_section "glossary" "Glossary"

# Create .gitbook.yaml
cat > .gitbook.yaml << EOL
root: ./docs/

structure:
  readme: README.md
  summary: SUMMARY.md
EOL

echo "Documentation structure has been created in the docs directory"
echo "Please run 'gitbook serve' to preview your documentation" 