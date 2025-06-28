#!/usr/bin/env python3
"""
MCP Sample Binary Application
A simple command-line tool demonstrating binary operations and file processing.
"""

import argparse
import sys
import os
from typing import List, Optional


class BinaryProcessor:
    """A class for handling binary operations and file processing."""
    
    def __init__(self):
        self.version = "1.0.0"
    
    def text_to_binary(self, text: str) -> str:
        """Convert text to binary representation."""
        return ' '.join(format(ord(char), '08b') for char in text)
    
    def binary_to_text(self, binary: str) -> str:
        """Convert binary representation back to text."""
        try:
            binary_values = binary.split()
            chars = [chr(int(b, 2)) for b in binary_values]
            return ''.join(chars)
        except ValueError as e:
            raise ValueError(f"Invalid binary format: {e}")
    
    def process_file(self, filepath: str, operation: str) -> str:
        """Process a file with the specified operation."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if operation == 'encode':
            return self.text_to_binary(content)
        elif operation == 'decode':
            return self.binary_to_text(content)
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    def save_output(self, content: str, output_path: str) -> None:
        """Save content to output file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Output saved to: {output_path}")


def main():
    """Main entry point for the binary processor application."""
    parser = argparse.ArgumentParser(
        description="MCP Sample Binary Application - Text/Binary converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --text "Hello World" --encode
  %(prog)s --file input.txt --decode --output result.txt
  %(prog)s --text "Hello" --encode --output binary.txt
        """
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--text', '-t', help='Input text to process')
    input_group.add_argument('--file', '-f', help='Input file to process')
    
    # Operation options
    operation_group = parser.add_mutually_exclusive_group(required=True)
    operation_group.add_argument('--encode', '-e', action='store_true',
                                help='Convert text to binary')
    operation_group.add_argument('--decode', '-d', action='store_true',
                                help='Convert binary to text')
    
    # Output options
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0.0')
    
    args = parser.parse_args()
    
    processor = BinaryProcessor()
    
    try:
        # Determine operation
        operation = 'encode' if args.encode else 'decode'
        
        # Process input
        if args.text:
            if operation == 'encode':
                result = processor.text_to_binary(args.text)
            else:
                result = processor.binary_to_text(args.text)
        else:
            result = processor.process_file(args.file, operation)
        
        # Handle output
        if args.output:
            processor.save_output(result, args.output)
        else:
            print(result)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
