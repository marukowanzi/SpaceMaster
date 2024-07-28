import socket
import replicate
import requests
import os

# def download_file(url, save_path):
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(save_path, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return save_path

def generate_image_and_model(prompt, image_url):
    print(f"Received prompt: {prompt}")
    print(f"Received image URL: {image_url}")
    input_text_to_image = {
        "seed": 25086,
        "image": image_url,
        "prompt": prompt,
        "condition_scale": 0.5,
        "num_inference_steps": 20
    }
    print("Running text-to-image generation...")
    output_image = replicate.run(
        "lucataco/sdxl-controlnet-depth:5e0a5cda895aa23a1aaa1a9a265220097102448e1b4c42b22a3c6d87c12d41a9",
        input=input_text_to_image
    )
    print(f"Generated image: {output_image}")

    if not isinstance(output_image, str):
        return "Error generating image"

    generated_image_url = output_image

    input_remove_bg = {
        "image": generated_image_url
    }
    print("Running background removal...")
    output_remove_bg = replicate.run(
        "lucataco/remove-bg:95fcc2a26d3899cd6c2691c900465aaeff466285a65c14638cc5f36f34befaf1",
        input=input_remove_bg
    )
    print(f"Background removed image: {output_remove_bg}")
    if not isinstance(output_remove_bg, str):
        return "Error removing background"

    removed_bg_image_url = output_remove_bg

    input_image_to_model = {
        "image_path": removed_bg_image_url,
        "do_remove_background": False
    }
    print("Running image-to-model generation...")

    output_model = replicate.run(
        "camenduru/tripo-sr:e0d3fe8abce3ba86497ea3530d9eae59af7b2231b6c82bedfc32b0732d35ec3a",
        input=input_image_to_model
    )

    print(f"Generated model: {output_model}")

    if not isinstance(output_model, str):
        return "Error generating 3D model"

    return output_model
    # 下载 GLB 文件
    # glb_save_path = os.path.join("F:\Apply for Phd Material\HCIX\TripoSR-Test\output", "generated_model.glb")
    # download_file(output_model, glb_save_path)
    # print(f"Downloaded GLB file to: {glb_save_path}")

    

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.23.68.138', 25001))
    server_socket.listen(1)
    print("Server is listening on port 25001...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        try:
            request = client_socket.recv(4096).decode('utf-8')
            if request:
                try:
                    print(f"Received request: {request}")
                    prompt, image_url = request.split(';')
                    result = generate_image_and_model(prompt, image_url)
                    print(f"Generated model URL: {result}")
                    client_socket.sendall(result.encode('utf-8'))
                except Exception as e:
                    error_message = f"Error processing request: {e}"
                    client_socket.sendall(error_message.encode('utf-8'))
        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
