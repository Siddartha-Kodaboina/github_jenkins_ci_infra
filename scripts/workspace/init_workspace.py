#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path

def setup_workspace(app_repo: str, app_name: str):
    """
    Sets up the workspace by cloning repositories and creating necessary directories
    """
    try:
        # Get the builds directory path (one level up from ci_infra)
        workspace_root = Path(os.getcwd()).parent
        
        print(f"Setting up workspace in: {workspace_root}")
        
        # Clone the application repository
        app_path = workspace_root / app_name
        if not os.path.exists(str(app_path)):
            subprocess.run(
                ["git", "clone", app_repo, str(app_path)], 
                check=True
            )
            print(f"Successfully cloned {app_name} repository")
        else:
            print(f"Application directory already exists: {app_path}")
            
        print("Workspace initialization completed successfully")
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"Error during git clone: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1

def main():
    parser = argparse.ArgumentParser(description="Initialize workspace for application build")
    parser.add_argument("--app-repo", required=True, help="Application repository URL")
    parser.add_argument("--app-name", required=True, help="Application name")
    
    args = parser.parse_args()
    
    return setup_workspace(args.app_repo, args.app_name)

if __name__ == "__main__":
    sys.exit(main())