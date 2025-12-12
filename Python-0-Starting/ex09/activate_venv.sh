#!/bin/bash

echo "Activando entorno virtual..."
source venv/bin/activate
echo "✓ Entorno virtual activado"
echo ""
echo "Paquete instalado:"
pip show ft_package
echo ""
echo "Para desactivar: deactivate"
