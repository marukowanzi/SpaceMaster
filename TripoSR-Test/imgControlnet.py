import replicate

image_path = "https://github.com/marukowanzi/imagebed/raw/00eab9f9328cf4cfa75a2414ea97f4f2d1826008/sofa.png"

input={
        "seed": 25086,
        "image": image_path,
        "prompt": "A soft sofa with Chinese decorative patterns, elegant, detailed embroidery, intricate floral motifs, traditional Chinese art style, luxurious fabric, rich colors, harmonious design, high-resolution, beautifully crafted, sophisticated, stylish",
        "negative_prompt": "Low quality, blurry, plain, modern style, Western motifs, abstract patterns, simplistic, monochromatic, poor craftsmanship, unrefined, pixelated, unattractive, minimalist design",
        "condition_scale": 0.5,
        "num_inference_steps": 20
    }

output = replicate.run(
    "lucataco/sdxl-controlnet-depth:5e0a5cda895aa23a1aaa1a9a265220097102448e1b4c42b22a3c6d87c12d41a9",
    input=input
)
print(output)
