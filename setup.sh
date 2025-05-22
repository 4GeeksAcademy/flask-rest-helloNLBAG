
echo "🔧 Iniciando setup del proyecto Star Wars Blog..."

echo "📦 Instalando dependencias..."
pipenv install sqlalchemy eralchemy2 graphviz python-dotenv

echo "🗃️  Creando base de datos..."
pipenv run python src/create_db.py

echo "🧩 Generando diagrama..."
pipenv run eralchemy -i sqlite:///src/example.db -o diagram.png --exclude-tables alembic_version

echo "✅ Todo listo. Archivo diagram.png generado con éxito."
