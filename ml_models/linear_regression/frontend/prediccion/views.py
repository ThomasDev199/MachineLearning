import requests
from django.conf import settings
from django.shortcuts import render
from .forms import PrediccionForm


def predecir(request):
    resultado = None
    error = None

    if request.method == "POST":
        form = PrediccionForm(request.POST)
        if form.is_valid():
            try:
                r = requests.post(
                    settings.API_PREDICT_URL,
                    json={"surface": form.cleaned_data["surface"]},
                    timeout=10,
                )
                r.raise_for_status()
                data = r.json()
                resultado = {
                    "m2": data["surface_m2"],
                    "precio": data["predicted_price_cop"],
                    "moneda": data["currency"],
                }
            except requests.exceptions.ConnectionError:
                error = "No se pudo conectar con el servicio de predicción. ¿Está corriendo FastAPI?"
            except requests.exceptions.Timeout:
                error = "El servicio de predicción tardó demasiado en responder."
            except requests.exceptions.HTTPError:
                error = "El servicio rechazó los datos enviados. Revisa el valor ingresado."
            except (KeyError, ValueError):
                error = "La respuesta del servicio no tiene el formato esperado."
    else:
        form = PrediccionForm()

    return render(request, "prediccion/predecir.html", {
        "form": form,
        "resultado": resultado,
        "error": error,
    })