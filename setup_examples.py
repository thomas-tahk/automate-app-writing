#!/usr/bin/env python3
"""
Setup Examples Script

This script copies the example files to the appropriate input directories 
to help users get started quickly.
"""

import os
import shutil
from pathlib import Path

def main():
    """Copy example files to input directories."""
    # Get the current directory
    current_dir = Path(__file__).parent
    examples_dir = current_dir / "examples"
    
    # Create input directories if they don't exist
    input_dirs = {
        "resumes": current_dir / "input" / "resumes",
        "cover_letters": current_dir / "input" / "cover_letters",
        "job_descriptions": current_dir / "input" / "job_descriptions"
    }
    
    for dir_name, dir_path in input_dirs.items():
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Copy example files
    example_files = {
        "resume_template.txt": input_dirs["resumes"] / "example_resume.txt",
        "cover_letter_template.txt": input_dirs["cover_letters"] / "example_cover_letter.txt",
        "job_description_sample.txt": input_dirs["job_descriptions"] / "acme_junior_dev.txt"
    }
    
    for src_name, dest_path in example_files.items():
        src_path = examples_dir / src_name
        if src_path.exists():
            shutil.copy2(src_path, dest_path)
            print(f"Copied {src_path.name} to {dest_path}")
        else:
            print(f"Warning: Example file not found: {src_path}")
    
    # Copy config sample
    config_src = examples_dir / "config_sample.json"
    config_dest = current_dir / "config.json"
    if config_src.exists():
        shutil.copy2(config_src, config_dest)
        print(f"Created configuration file: {config_dest}")
    
    print("\nSetup complete!")
    print("You can now modify the example files in the input directories and run:")
    print("  python tailor_documents.py")
    print("\nOr to process a specific job:")
    print("  python tailor_documents.py --job acme_junior_dev")

if __name__ == "__main__":
    main() 