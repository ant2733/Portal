import sys
import shutil
import os
from tkinter import Tk, filedialog
import json

def main():
    if len(sys.argv) > 1:
        # 调用json里面的数据
        with open(config_path, 'r') as f:
            data = json.load(f)
        target_path = data["last_path"]
            
        source = sys.argv[1]
        destination_dir = f"{target_path}"
        
        # 移动文件
        shutil.move(source, destination_dir)
    else:
        floder_path = select_folder()
        set_path(config_path, floder_path)



# 储存记忆选择的路径
appdata_dir = os.getenv('APPDATA')      # 获取Windows系统预设的路径

# 在这个路径下创建子目录
config_dir = os.path.join(appdata_dir, "portal")
os.makedirs(config_dir, exist_ok=True)      # 当目录不存在时创建目录

config_path = os.path.join(config_dir, "setting.json")
def set_path(config_path, path):
    """修改json文件"""
    with open(config_path, 'w') as f:
        json.dump({"last_path": path}, f)
    return 




def select_folder():
    """选择路径"""
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    # 调用文件夹选择对话框
    folder_path = filedialog.askdirectory(
        title="选择目标文件夹"
    )
    root.destroy()
    return folder_path if folder_path else None  # 返回路径或None（用户取消）



if __name__ == "__main__":
    main()


