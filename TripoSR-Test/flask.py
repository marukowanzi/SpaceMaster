from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 设置上传文件夹
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        # 保存文件
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        # 生成文件的 URL
        file_url = f"http://yourserver.com/{UPLOAD_FOLDER}/{file.filename}"
        
        # 打印返回的 URL 进行调试
        print("File URL:", file_url)
        
        return file_url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
