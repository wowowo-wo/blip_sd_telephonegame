import os
from PIL import Image
import argparse
from .model import image_to_caption, caption_to_image

def main(args):

    os.makedirs(args.prefix, exist_ok=True)
    initial_output_path = os.path.join(args.output_prefix, f"{args.prefix}_step_0.png")
    init_img = Image.open(args.image_path).convert("RGB")
    init_img = init_img.resize((1024, 1024))
    init_img.save(initial_output_path)
    image_path = initial_output_path

    caption_log_path = os.path.join(args.output_prefix, "captions.txt")
    with open(caption_log_path, "w") as f:
        f.write(f"step_0: (original image)\n")

    for i in range(args.steps):
        print(f"Step {i+1}")
        caption = image_to_caption(
            image_path,
            min_len=args.min_length,
            max_len=args.max_length,
            num_bms=args.num_beams,
            no_repeat_ngram=args.no_repeat_ngram_size
        )

        print(f"Caption: {caption}")

        with open(caption_log_path, "a") as f:
            f.write(f"step_{i+1}: {caption}\n")

        output_image_path = os.path.join(args.output_prefix, f"{args.output_prefix}_step_{i+1}.png")
        image_path = caption_to_image(caption, output_image_path)

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", type=str, required=True, help="file path of an input image")
    parser.add_argument("--steps", type=int, default=10, help="number of loops")
    parser.add_argument("--min_length", type=int, default=30, help="minimum length of caption")
    parser.add_argument("--max_length", type=int, default=100, help="maxium length of caption")
    parser.add_argument("--num_beams", type=int, default=5, help="number of beams")
    parser.add_argument("--no_repeat_ngram_size", type=int, default=2, help="size of no repeat n-gram")
    parser.add_argument("--output_prefix", type=str, default="output", help="generated images are saved as 'prefix/prefix_step_i.png'")

    args = parser.parse_args()
    
    return args