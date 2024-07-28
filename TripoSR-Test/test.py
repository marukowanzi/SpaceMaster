import subprocess

def check_nvcc_version():
    try:
        # 使用 subprocess 运行 nvcc --version 命令
        result = subprocess.run(['nvcc', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # 成功运行，打印版本信息
            print(result.stdout)
        else:
            # 命令运行失败，打印错误信息
            print("Error: ", result.stderr)
    except FileNotFoundError:
        print("nvcc is not installed or not found in PATH.")

if __name__ == "__main__":
    check_nvcc_version()

