
#!/bin/bash

FECHA=$(date +%F)

cp -r modulo-1/datos "modulo-1/respaldo-$FECHA"

echo "Respaldo creado correctamente: respaldo-$FECHA"
