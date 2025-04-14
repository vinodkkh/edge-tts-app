import gradio as gr
import edge_tts
import asyncio
import uuid
import os

async def generate_audio(text, voice):
    filename = f"tts_{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(filename)
    return filename

def tts_wrapper(text, voice):
    return asyncio.run(generate_audio(text, voice))

# You can replace or expand this list with full voice list
voices = [
    "en-US-GuyNeural", "en-US-JennyNeural",
    "hi-IN-MadhurNeural", "hi-IN-SwaraNeural"
]

app = gr.Interface(
    fn=tts_wrapper,
    inputs=[
        gr.Textbox(label="Enter Text", lines=4),
        gr.Dropdown(choices=voices, label="Voice", value="en-US-GuyNeural")
    ],
    outputs=gr.Audio(type="filepath"),
    title="Edge-TTS App (Free)",
    description="Convert text to speech using Microsoft Edge TTS voices."
)
import os

port = int(os.environ.get("PORT", 8080))  # Render assigns this
app.launch(server_name="0.0.0.0", server_port=port, share=False)




