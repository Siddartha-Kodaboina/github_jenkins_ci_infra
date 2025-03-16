#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path

def build_application(app_name: str, workspace_root: str):
    """
    Builds the application using Docker
    """
    try:
        # Get the application directory path (two levels up from current script and into app directory)
        workspace_path = Path(workspace_root)
        app_path = workspace_path / app_name / app_name
        
        print(f"Building application in: {app_path}")
        
        # Change to application directory
        os.chdir(str(app_path))
        
        # Build Docker image
        image_name = f"{app_name}:latest"
        subprocess.run(
            ["docker", "build", "-t", image_name, "."],
            check=True
        )
        
        print(f"Successfully built Docker image: {image_name}")
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"Error during docker build: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1

def main():
    parser = argparse.ArgumentParser(description="Build application Docker image")
    parser.add_argument("--workspace-root", required=True, help="Workspace root Path")
    parser.add_argument("--app-name", required=True, help="Application name")
    
    args = parser.parse_args()
    
    return build_application(args.app_name, args.workspace_root)

if __name__ == "__main__":
    sys.exit(main())