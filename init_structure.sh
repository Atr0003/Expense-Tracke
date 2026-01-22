#!/usr/bin/env bash
set -euo pipefail

echo "📁 Initialisation de la structure MVC/MVP à la racine du dépôt..."

# Dossiers principaux
mkdir -p src tests docs

# Application / bootstrap
mkdir -p src/app
touch src/app/{config.env.example,bootstrap.md}

# Couches applicatives
mkdir -p src/{controllers,views,services,domain,repositories}
touch src/controllers/.gitkeep
touch src/views/.gitkeep
touch src/services/.gitkeep
touch src/domain/.gitkeep
touch src/repositories/.gitkeep

# Points d’entrée & documentation interne
touch src/{main.md,README_structure.md}

# Tests
mkdir -p tests/{unit,integration}
touch tests/unit/.gitkeep
touch tests/integration/.gitkeep

# Documentation projet
touch docs/{architecture.md,decisions.md}

# Fichiers racine usuels (vides)
touch README.md .gitignore

echo "✅ Structure créée avec succès à la racine."
echo
echo "📂 Dossiers:"
find . -maxdepth 2 -type d | sort
echo
echo "📄 Fichiers:"
find . -maxdepth 2 -type f | sort
