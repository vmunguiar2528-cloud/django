# ERP Project

Proyecto Django de ERP con módulos de clientes, proveedores, productos, ventas y reportes.

## Requisitos

- Python 3.10+
- Django
- SQLite3

## Instalación

1. Crear entorno virtual
   ```powershell
   py -m venv env_erp
   .\env_erp\Scripts\Activate.ps1
   ```

2. Instalar dependencias
   ```powershell
   pip install -r requirements.txt
   ```

3. Aplicar migraciones
   ```powershell
   python manage.py migrate
   ```

4. Ejecutar proyecto
   ```powershell
   python manage.py runserver
   ```

5. Abrir en navegador
   ```text
   http://127.0.0.1:8000/
   ```

## Subir a GitHub

```powershell
git init
git add .
git commit -m "Proyecto ERP inicial"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

Si el repositorio ya existe:

```powershell
git remote set-url origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```

## Importante

- Reemplaza `TU_USUARIO` y `TU_REPO` por tu usuario y nombre real del repositorio en GitHub.
- No uses un email o dominio como parte de la URL.
- Si te aparece un error de identidad de Git, corre:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```
