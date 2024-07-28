import replicate
from dotenv import load_dotenv
from pprint import pprint 
import requests
import json
import threading
from dataclasses import dataclass
import socket

load_dotenv()
host, port = "10.23.68.138", 25001

def download_image(image_url, filename):
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print("Failure!!!")

def handle_client(client_socket):
    while True:
        try:
            # 接收客户端发送的消息
            prompt = client_socket.recv(1024).decode('utf-8').strip()
            if not prompt:
                break
            print(f"Received prompt: {prompt}")

            # 调用Replicate生成图像URL
            output = replicate.run(
                "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
                input={"prompt": prompt}
            )

            pprint(output)
            image_url = output[0]
            download_image(image_url, "output.jpg")

            # 发送图像URL给客户端
            client_socket.sendall((image_url + '\n').encode('utf-8'))
            print(f"Sent image URL: {image_url}")
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def main():
    host, port = "10.23.68.138", 25001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, _ = server_socket.accept()
        print("Client connected")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

