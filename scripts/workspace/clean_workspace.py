#!/usr/bin/env python3

import shutil
import sys
from pathlib import Path

def clean_workspace():
    """
    Cleans up the workspace
    """
    try:
        workspace_root = Path(os.getcwd()).parent
        
        # Only remove contents, not the directory itself
        for item in workspace_root.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
                
        print("Workspace cleaned successfully")
        return 0
        
    except Exception as e:
        print(f"Error cleaning workspace: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(clean_workspace())