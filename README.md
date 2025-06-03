# blip_sd_telephonegame

<img src="ex/okcomp_merged.png" width = 1200>

<img src="ex/dbell_merged.png" width = 1200>

<img src="ex/sss_merged.png" width = 1200>

This is an experimental and funny project exploring how meaning shifts and noise accumulate when an image is repeatedly passed two different kinds of AI models.

flow is simple:
Start with an image, turn it into a caption using BLIP, then use Stable Diffusion to generate a new image from that caption. That image is again turned into a caption by BLIP ... and so on. It`s like a "telephone game"

While more advanced models like BLIP-2 or GPT-4V might produce more stable or intelligent results, this project deliberately uses BLIP and SDXL1.0 for their reproducibility and light computational cost. In fact, The glitches and weirdness are more interesting and more desirable than precision.

The header images were created using this loop, starting from famous album covers:  
Radiohead’s "OK Computer", Pink Floyd’s "The Division Bell", and Yellow Magic Orchestra’s "Solid State Survivor".  


## Usage

clone this repo and install the requirements:

```bash
git clone https://github.com/wowowo-wo/blip_sd_telephonegame
cd blip_sd_telephonegame
pip install -r requirements.txt
```

and run in CLI:
```bash
python3 cli.py --image_path PATH_to_image --steps 10 --min_length 30 --max_length 100 --num_beams 5 --no_repeat_ngram_size 2 --output_prefix output
```
## Observation of the above examples



In the example of "OK Computer", a very breathtaking transformation can be seen.
Initially, the letters "OK" are interpreted as an O wrapping around a K, which then changes into a pattern in a circle in nature. 

The highway element in the original image remains as concrete buildings symbolizing an artificial object, but soon fades away.
After that, the circular pattern in the square change into a clock, and people start to gather. 

A large tree emerges at the center of the previously flat square, and the circle which is originally "O" changes into a halo of the tree.
Finally, a large tree by a lake appears, with people gathered beneath it. 

This transformation is extremely compelling, including the contrast with OK Computer, which is an album with a disturbing, eerie, and dark atmosphere throughout.

---

"The Division Bell" example produces an unexpected result. When people view the cover of this album, the most striking element is the split-faced object. 

The abstract face is immediately replaced by a realistic human figure.  The theme of "pairing" continues for a while, but eventually shifts to three figures, and then to a single individual.

The one consistent element throughout is the backdrop of blue sky and expansive natural scenery.

---

"Solid State Survivor" example is open to some interpretation. The cover is a striking composition, depicting the members of YMO in red suits, sitting in a light-green room. 

At first, BLIP correctly “recognizes” the scene, and SD generates an image of people in red suits seated around a table in front of a green screen. 

However, perhaps due to the unusual nature of red suits, in the next image only one woman remains in red, while the others wear plain-colored outfits. In the following image, the red clothing disappears entirely. 
The light-green room persists for a while as a green screen, but eventually vanishes—replaced by a man whose suit has turned green. 

The one element that remained consistent was the image of a man sitting in a chair.



## How to Make the Captions Weirder

The key to interesting output often lies in tweaking how the caption is generated from the image.

The BLIP model supports parameters like: min_length, max_length, num_beams, no_repeat_ngram_size

To encourage more hallucination and unexpected results, increasing min_length and reducing num_beams can be expected to be effective measure. Because, that forces BLIP to generate a longer caption, but with fewer options to refine it leading to stranger, more surprising descriptions. So, The AIs start trying to see things that might not really be there.

## Requirements

torch
torchvision
transformers
diffusers
accelerate
pillow
