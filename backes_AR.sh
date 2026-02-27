#!/bin/bash

# Directorio donde se guardarán los respaldos
BACKUP_DIR="backup_es_AR_$(date +%Y%m%d_%H%M%S)"

echo "Creando directorio de respaldo: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# Función para buscar y mover manteniendo la estructura de carpetas
backup_and_remove() {
    local target_dir=$1
    if [ -d "$target_dir" ]; then
        echo "Buscando en $target_dir..."
        find "$target_dir" -type f -name "es_AR.csv" | while read -r file; do
            # Crear la estructura de directorios dentro de la carpeta de backup
            mkdir -p "$BACKUP_DIR/$(dirname "$file")"

            # Mover el archivo al directorio de backup
            mv "$file" "$BACKUP_DIR/$file"
            echo "Movido: $file"
        done
    else
        echo "El directorio $target_dir no existe. Omitiendo..."
    fi
}

# Ejecutar para 'app' y 'vendor'
backup_and_remove "app"
backup_and_remove "vendor"

echo "¡Proceso completado! Todos los archivos es_AR.csv fueron movidos a $BACKUP_DIR"