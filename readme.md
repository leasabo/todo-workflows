# Automatización con Triggers de GitHub Actions

Esta es una aplicación de lista de tareas simple en Python, utilizada como base para demostrar el funcionamiento de 6 tipos distintos de triggers en GitHub Actions.

## Los 6 Workflows de GitHub Actions

### 1. Trigger por Push: `01-push.yml`

Se activa automáticamente cada vez que se hace un `git push` a la rama `master`.

**Mensaje que imprime:**
```
Workflow activado por push
```
<img width="1006" height="703" alt="01_push" src="https://github.com/user-attachments/assets/06c74bf2-be5d-4a8a-818b-4caa1689888b" />

---

### 2. Trigger por Pull Request: `02-pull_request.yml`

Se activa cuando se abre un Pull Request hacia la rama `master`.

**Mensaje que imprime:**
```
Pull request detectado
```
<img width="1006" height="705" alt="02_pull_request" src="https://github.com/user-attachments/assets/e95a1a72-b992-451a-b99a-78cc65683788" />

---

### 3. Trigger por Issues: `03-issues.yml`

Se activa cuando alguien crea un nuevo Issue en el repositorio.

**Mensaje que imprime:**
```
Nuevo issue creado
```
<img width="1006" height="723" alt="03_issues" src="https://github.com/user-attachments/assets/a6c03355-b70d-4ae7-b33a-f13a11cb92e8" />

---

### 4. Trigger por Comentario en PR: `04-issue_comment.yml`

Se activa cuando alguien comenta en un issue o PR, pero **solo ejecuta el job si el comentario es en un Pull Request** (se filtra con la condición `if: github.event.issue.pull_request != null`).

**Mensaje que imprime:**
```
Comentario en PR detectado
```
<img width="1006" height="707" alt="04_issue_comment" src="https://github.com/user-attachments/assets/aa022975-a75b-49f3-94df-55257b685fd1" />

---

### 5. Trigger Manual: `05-workflow_dispatch.yml`

Permite ejecutar el workflow manualmente desde la pestaña **Actions** de GitHub, con un input de tipo `choice` para seleccionar el nivel de alerta.

**Opciones disponibles:** `bajo`, `medio`, `alto`, `critico`

**Mensaje que imprime:**
```
Nivel de alerta seleccionado: [opción elegida]
```
<img width="1006" height="405" alt="05_workflow_dispatch" src="https://github.com/user-attachments/assets/706bbb75-a2b2-4a4c-8cf3-3561939b9d19" />

---

### 6. Trigger Programado: `06-schedule.yml`

Se ejecuta automáticamente **cada hora** según el cron `0 * * * *`.

**Mensaje que imprime:**
```
Ejecución programada
```
<img width="1006" height="684" alt="06_schedule" src="https://github.com/user-attachments/assets/7f2078d3-a024-4157-8341-c68cdd9c6d03" />

---
