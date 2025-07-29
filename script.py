input_path = 'Tresc.md'
output_path = 'Tresc_v2.md'

with open(input_path, 'r', encoding='utf-8') as file:
    content = file.read()

count = 1
def replacer(match):
    global count
    result = f"[Fig.{count}]"
    count += 1
    return result

import re
content = re.sub(r'\[Fig\.\]', replacer, content)

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(content)

print("Done.")
