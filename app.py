import gradio as gr
import requests
import os

def generar_imagen(prompt):
    api_token = os.getenv("REPLICATE_API_TOKEN")
    if not api_token:
        return "⚠️ Error: No se encontró la API KEY."

    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "version": "f1786cf27a31d845a5f1699da7aab109c439c5769113eb9c07c62352b0ecd5c0",
        "input": {
            "prompt": prompt
        }
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        prediction_url = response_json.get("urls", {}).get("get")
        if not prediction_url:
            return "⚠️ Error al obtener la imagen."

        while True:
            result = requests.get(prediction_url, headers=headers).json()
            status = result.get("status")
            if status == "succeeded":
                return result["output"][0]
            elif status == "failed":
                return "⚠️ Falló la generación de imagen."
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=generar_imagen,
    inputs=gr.Textbox(label="Describe tu imagen mágica 🧠✨"),
    outputs=gr.Image(type="filepath", label="Resultado"),
    title="Ayala: Generadora de Magia I.A",
    description="Transforma tu imaginación en arte visual usando IA. 🔮"
)

demo.launch()
