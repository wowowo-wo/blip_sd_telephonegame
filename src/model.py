from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from diffusers import StableDiffusionXLPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

pipe = StableDiffusionXLPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",torch_dtype=torch.float16).to(device)

def image_to_caption(image_path,min_len=30, max_len=100, num_bms=5, no_repeat_ngram=2):
    raw_image = Image.open(image_path).convert("RGB")
    inputs = processor(raw_image, return_tensors="pt").to(device)

    out = model.generate(
        **inputs,
        min_length=min_len,
        max_length=max_len,
        num_beams=num_bms,
        no_repeat_ngram_size=no_repeat_ngram,
        early_stopping=True
    )

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def caption_to_image(caption, output_path):
    image = pipe(prompt=caption).images[0]
    image.save(output_path)
    return output_path

