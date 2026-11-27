# Railway: frontend y backend en un servicio

El servicio combinado mantiene FastAPI en `/predict` y `/docs`, y sirve la página Django en `/`.

## Configuración del servicio existente

- **Root Directory:** `/ml_models/linear_regression`
- **Start Command:** `python frontend/manage.py collectstatic --noinput && uvicorn main:app --app-dir backend --host 0.0.0.0 --port $PORT`
- **Variable:** `DJANGO_SECRET_KEY`, con una clave privada aleatoria.

La app llama a FastAPI por el puerto local del mismo servicio. No configures `API_PREDICT_URL` para apuntar al dominio público.

Guarda los cambios, sube los archivos del proyecto a la rama conectada con Railway y despliega. Al finalizar, `/` abre el frontend y `/docs` conserva la documentación de la API.
