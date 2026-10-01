import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import random

def create_comic_text(text):
    # Create image
    img = Image.new('RGB', (800, 400), color=(255, 230, 0))
    draw = ImageDraw.Draw(img)
    
    # Try to use a bold font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()
    
    # Draw comic style text
    draw.text((50, 150), text.upper(), fill=(255,0,0), stroke_width=4, stroke_fill=(0,0,0), font=font)
    return img

demo = gr.Interface(
    fn=create_comic_text,
    inputs=gr.Textbox(label="Un text-a type pannu", placeholder="DEI MASSU DA!"),
    outputs=gr.Image(label="ComicCraft Output"),
    title="ComicCraft-AI"
)

demo.launch()