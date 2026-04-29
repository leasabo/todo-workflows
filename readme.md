# Automatización con Triggers de GitHub Actions

Esta es una aplicación de lista de tareas simple en Python, utilizada como base para demostrar el funcionamiento de 6 tipos distintos de triggers en GitHub Actions.

## Los 6 Workflows de GitHub Actions

### 1. `01-push.yml` — Trigger por Push

Se activa automáticamente cada vez que se hace un `git push` a la rama `master`.

**Mensaje que imprime:**
```
Workflow activado por push
```

---

### 2. `02-pull_request.yml` — Trigger por Pull Request

Se activa cuando se abre un Pull Request hacia la rama `master`.

**Mensaje que imprime:**
```
Pull request detectado
```

---

### 3. `03-issues.yml` — Trigger por Issues

Se activa cuando alguien crea un nuevo Issue en el repositorio.

**Mensaje que imprime:**
```
Nuevo issue creado
```

---

### 4. `04-issue_comment.yml` — Trigger por Comentario en PR

Se activa cuando alguien comenta en un issue o PR, pero **solo ejecuta el job si el comentario es en un Pull Request** (se filtra con la condición `if: github.event.issue.pull_request != null`).

**Mensaje que imprime:**
```
Comentario en PR detectado
```

---

### 5. `05-workflow_dispatch.yml` — Trigger Manual

Permite ejecutar el workflow manualmente desde la pestaña **Actions** de GitHub, con un input de tipo `choice` para seleccionar el nivel de alerta.

**Opciones disponibles:** `bajo`, `medio`, `alto`, `critico`

**Mensaje que imprime:**
```
Nivel de alerta seleccionado: [opción elegida]
```

---

### 6. `06-schedule.yml` — Trigger Programado

Se ejecuta automáticamente **cada hora** según el cron `0 * * * *`.

**Mensaje que imprime:**
```
Ejecución programada
```

---
