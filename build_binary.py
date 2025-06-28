#!/usr/bin/env python3
"""
Build script to create standalone binary executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_pyinstaller():
    """Check if PyInstaller is installed."""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False


def install_pyinstaller():
    """Install PyInstaller using pip."""
    print("Installing PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])


def build_binary():
    """Build the binary executable."""
    script_dir = Path(__file__).parent
    main_script = script_dir / "main.py"
    dist_dir = script_dir / "dist"
    build_dir = script_dir / "build"
    
    # Clean previous builds
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    if build_dir.exists():
        shutil.rmtree(build_dir)
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--name=mcp-binary",  # Name of the executable
        "--console",  # Console application
        "--clean",  # Clean cache before building
        str(main_script)
    ]
    
    print("Building binary executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd, cwd=script_dir)
        print("\n✅ Binary built successfully!")
        
        # Show the location of the binary
        binary_path = dist_dir / "mcp-binary"
        if sys.platform == "win32":
            binary_path = binary_path.with_suffix(".exe")
        
        if binary_path.exists():
            print(f"📁 Binary location: {binary_path.absolute()}")
            print(f"📏 Binary size: {binary_path.stat().st_size / (1024*1024):.1f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)


def main():
    """Main build function."""
    print("🔨 MCP Binary Builder")
    print("=" * 40)
    
    # Check if PyInstaller is available
    if not check_pyinstaller():
        print("PyInstaller not found. Installing...")
        install_pyinstaller()
    
    # Build the binary
    build_binary()
    
    print("\n🎉 Build complete!")
    print("\nTo test the binary:")
    print('  ./dist/mcp-binary --text "Hello World" --encode')
    print('  ./dist/mcp-binary --help')


if __name__ == "__main__":
    main()
