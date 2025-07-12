import os
import requests
import gradio as gr

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

def generar_imagen(prompt):
    if not STABILITY_API_KEY:
        return "⚠️ API KEY no encontrada."

    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code != 200:
            return f"❌ Error: {response.status_code} - {response.text}"

        data = response.json()
        if not data.get("artifacts"):
            return "❌ No se recibió imagen."

        image_data = data["artifacts"][0]["base64"]
        image_path = "/tmp/imagen_generada.png"
        with open(image_path, "wb") as f:
            f.write(bytes.fromhex(image_data))

        return image_path

    except Exception as e:
        return f"❌ Excepción: {str(e)}"

demo = gr.Interface(
    fn=generar_imagen,
    inputs=gr.Textbox(label="Describe tu imagen mágica ✨"),
    outputs=gr.Image(type="filepath", label="Resultado"),
    title="Ayala: Generadora de Magia I.A",
    description="Transforma tu imaginación en arte visual usando SDXL ✨🖼️"
)

demo.launch()
