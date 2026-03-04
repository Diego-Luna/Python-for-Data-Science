#!/bin/bash

echo "activate virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"
echo ""
echo "Installed package:"
pip show ft_package
echo ""
echo "To deactivate: deactivate"
