from __future__ import with_statement
import logging
from logging.config import fileConfig
from flask import current_app
from alembic import context

# Carga la configuración de logging
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Extrae metadata del objeto db de tu app Flask
from models import db  # asegurándote de que esté importado desde src si es necesario
target_metadata = db.metadata

# Función para ejecutar migraciones
def run_migrations_offline():
    """Ejecuta migraciones sin una conexión directa."""
    url = current_app.config.get("SQLALCHEMY_DATABASE_URI")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta migraciones con conexión a la base de datos."""
    connectable = current_app.extensions['migrate'].db.engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
