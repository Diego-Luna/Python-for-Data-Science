#!/bin/bash

# ! Check if .venv exists, if not create it
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

#  Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"

# * Install build tools
pip install --upgrade pip build wheel > /dev/null 2>&1

echo ""
echo "Building package..."
python3 -m build > /dev/null 2>&1

echo ""
echo "Installing package..."
pip install ./dist/ft_package-0.0.1-py3-none-any.whl > /dev/null 2>&1

echo ""
echo "Installed package info:"
pip show -v ft_package
echo ""
echo "To deactivate: deactivate"
