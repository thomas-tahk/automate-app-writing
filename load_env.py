#!/usr/bin/env python3
"""
Environment Variable Loader for Automate App Writing

This script loads environment variables from a .env file or env.txt file
to make it easy to configure the API keys and other settings.
"""

import os
import sys
from pathlib import Path

def load_env_file(env_path):
    """Load environment variables from a file."""
    if not os.path.exists(env_path):
        print(f"Environment file not found: {env_path}")
        return False
    
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
                
            # Parse key-value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if value and (value[0] == value[-1] == '"' or value[0] == value[-1] == "'"):
                    value = value[1:-1]
                    
                # Set environment variable
                os.environ[key] = value
                print(f"Set environment variable: {key}")
    
    return True

def main():
    """Find and load environment file."""
    # Look for different possible env files
    current_dir = Path(__file__).parent
    possible_files = [
        current_dir / '.env',
        current_dir / 'env.txt',
        current_dir / 'env',
        current_dir / 'env.example'
    ]
    
    # Try to load from each possible location
    for env_path in possible_files:
        if load_env_file(env_path):
            print(f"Loaded environment from {env_path}")
            return True
    
    print("No environment file found. Please create a .env file or env.txt file.")
    print("You can copy the env.example file to start with.")
    return False

if __name__ == "__main__":
    main() 