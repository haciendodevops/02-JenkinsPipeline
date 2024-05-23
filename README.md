# Configuración de Jenkins para Usar el Jenkinsfile

## Paso 1: Configurar Jenkins para Usar el Jenkinsfile

### Crear un Multibranch Pipeline Job

1. En Jenkins, crea un nuevo Job y selecciona "Multibranch Pipeline".

### Configurar la Multibranch Pipeline

1. En la sección **Branch Sources**, añade tu repositorio GitHub.
2. Configura las credenciales si es necesario.
3. En la sección **Build Configuration**, selecciona "by Jenkinsfile".
4. Configura la detección de cambios para que se ejecute en todas las ramas que coincidan con los patrones `dev`, `task/*`, y `features/*`.

## Paso 2: Probar el Pipeline

### Realizar cambios en `app.py`

1. Por ejemplo, cambia el mensaje de salida a "Dummy2 Test in DevOps".

2. Haz un commit en el código y pushea a una rama (esto lo haría el programador, pero a modo de testeo, ya que es fácil, se puede hacer):

    ```sh
    git checkout -b features/update-message
    git add app.py
    git commit -m "Update message to Dummy2"
    git push origin features/update-message
    ```

## Paso 3: Verificar Jenkins

### Monitorear Jenkins

1. Jenkins debería detectar automáticamente el cambio y ejecutar el pipeline para la rama `features/update-message`.
2. Observa el proceso en Jenkins para asegurarte de que el contenedor Docker se construye y despliega correctamente con el nuevo mensaje.

Con estos pasos, habrás configurado Jenkins en un contenedor Docker con acceso al Docker del host, y configurado un pipeline que detecta automáticamente los cambios en las ramas especificadas, construye y despliega la nueva versión de tu aplicación Docker.
