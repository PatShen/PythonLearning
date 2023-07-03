#!/usr/bin/python
import os
import re

folder_path = "path_of_file"
allowed_extensions = (".h", ".m", ".swift")
pattern = r"(?m)((?:Copyright \(c\)|©) \d{4} )(.*?)( All rights reserved\.)"

def replace_callback(match):
    start = match.group(1)
    content = match.group(2)
    end = match.group(3)

    # 替换以 "AXX" 开头，以任意字符结尾的字符串为 "BXX."
    replaced_content = re.sub(r"^AXX(.*?)\.$", r"BXX.", content, flags=re.MULTILINE)

    return start + replaced_content + end

#遍历文件夹中的文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 检查文件扩展名
        if file.endswith(allowed_extensions):
            file_path = os.path.join(root, file)

            # 读取文件内容
            with open(file_path, 'r') as f:
                content = f.read()

            # 进行替换
            replaced_content = re.sub(pattern, replace_callback, content)

            # 将修改后的内容写回文件
            with open(file_path, 'w') as f:
                f.write(replaced_content)
