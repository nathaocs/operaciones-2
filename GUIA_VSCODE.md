# Guía: Cómo Activar los Prompts en Visual Studio Code

## ¿Qué son los "prompts"?

Los "prompts" son las solicitudes de entrada que hace tu programa de Python usando `input()`. Por ejemplo:
```python
a = int(input("Ingresa un numero"))
```

## Configuración Incluida

Este repositorio ahora incluye configuraciones de Visual Studio Code para ejecutar correctamente programas de Python con prompts.

### Archivos de Configuración

1. **`.vscode/settings.json`**: Configuración general del editor
2. **`.vscode/launch.json`**: Configuración de depuración
3. **`.vscode/extensions.json`**: Extensiones recomendadas

## Cómo Usar los Prompts en VS Code

### Opción 1: Ejecutar en Terminal (Recomendado)

1. Abre el archivo Python que quieres ejecutar (ej: `README.md`, `AREATT.py`, etc.)
2. Presiona **Ctrl + `** (backtick) para abrir el terminal integrado
3. Ejecuta el archivo con: `python3 nombre_del_archivo.py`
4. Los prompts aparecerán en el terminal y podrás escribir tus respuestas

**Ejemplo:**
```bash
python3 README.md
Ingresa un numero: 5
Ingresa un numero: 3
8
```

### Opción 2: Usar el Depurador (Para debugging)

1. Abre el archivo Python que quieres depurar
2. Presiona **F5** o ve a "Run and Debug" en el panel lateral
3. Selecciona la configuración correspondiente:
   - "Python: Archivo actual" - Para el archivo que estás viendo
   - "Python: AREATT" - Para el script de área de triángulo
   - "Python: Resta" - Para el script de resta
4. Los prompts aparecerán en el terminal integrado

### Opción 3: Botón "Run" (Requiere extensión Code Runner)

1. Instala la extensión "Code Runner" desde el marketplace
2. Abre tu archivo Python
3. Click derecho → "Run Code" o presiona **Ctrl+Alt+N**
4. Los prompts aparecerán en el terminal

## Extensiones Recomendadas

El archivo `.vscode/extensions.json` recomienda instalar:

- **Python** (ms-python.python): Soporte básico de Python
- **Pylance** (ms-python.vscode-pylance): Intellisense mejorado
- **Debugpy** (ms-python.debugpy): Depurador de Python
- **GitHub Copilot** (github.copilot): Asistente de código AI (opcional)
- **GitHub Copilot Chat** (github.copilot-chat): Chat con Copilot (opcional)

VS Code te sugerirá instalar estas extensiones automáticamente cuando abras el proyecto.

## Solución de Problemas

### Los prompts no aparecen

**Problema**: Cuando ejecuto mi programa, no veo donde escribir.

**Solución**: 
- Asegúrate de usar el terminal integrado (Ctrl + `)
- Verifica que `"console": "integratedTerminal"` esté en launch.json
- No uses el panel de "Output", usa el "Terminal"

### Error: "python no reconocido"

**Problema**: VS Code dice que no encuentra Python.

**Solución**:
1. Instala Python desde python.org
2. En Windows, agrega Python al PATH durante la instalación
3. Reinicia VS Code después de instalar Python
4. Verifica con: `python3 --version` o `python --version`

### Los prompts se ejecutan pero no veo la entrada

**Problema**: El programa corre pero no puedo ver lo que escribo.

**Solución**:
- Haz click en el terminal antes de escribir
- Verifica que la configuración `"runInTerminal": true` esté en settings.json

## Atajos de Teclado Útiles

- **Ctrl + `**: Abrir/cerrar terminal integrado
- **F5**: Iniciar depuración
- **Ctrl + F5**: Ejecutar sin depurar
- **Shift + F5**: Detener depuración
- **Ctrl + Alt + N**: Ejecutar código (con Code Runner)

## Ejemplo Completo

Para ejecutar el archivo `README.md` que contiene la calculadora:

1. Abre Visual Studio Code en este repositorio
2. Abre el archivo `README.md`
3. Presiona `Ctrl + `` para abrir terminal
4. Escribe: `python3 README.md`
5. Cuando veas "Ingresa un numero", escribe un número y presiona Enter
6. Repite para el segundo número
7. Verás el resultado de la suma

## Notas Adicionales

- Todos los archivos Python en este proyecto usan `input()` para solicitar datos
- La configuración está optimizada para permitir entrada interactiva
- El terminal integrado es la forma más confiable de manejar prompts
- Los debuggers también funcionan correctamente con prompts gracias a `"console": "integratedTerminal"`

## Recursos Adicionales

- [Documentación oficial de Python en VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Debugging Python en VS Code](https://code.visualstudio.com/docs/python/debugging)
- [Terminal integrado de VS Code](https://code.visualstudio.com/docs/terminal/basics)
