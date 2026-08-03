import re

with open('build_final_dataset.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '"image": "assets/images/image4.jpg"': '"image": "assets/images/proj-1.png"',
    '"image": "assets/images/image5.jpg"': '"image": "assets/images/proj-2.png"',
    '"image": "assets/images/image6.jpg"': '"image": "assets/images/proj-3.png"',
    '"image": "assets/images/image8.jpg"': '"image": "assets/images/proj-4.png"',
    '"image": "assets/images/image9.jpg"': '"image": "assets/images/proj-5.png"',
    '"image": "assets/images/image10.jpg"': '"image": "assets/images/park-1.png"',
    '"image": "assets/images/image11.jpg"': '"image": "assets/images/park-2.png"',
    '"image": "assets/images/image12.jpg"': '"image": "assets/images/park-3.png"',
    '"image": "assets/images/image13.jpg"': '"image": "assets/images/park-4.png"',
    '"image": "assets/images/image14.jpg"': '"image": "assets/images/park-5.png"',
    '"image": "assets/images/image15.jpg"': '"image": "assets/images/park-6.png"',
    '"image": "assets/images/image16.jpg"': '"image": "assets/images/park-7.png"',
    '"image": "assets/images/image17.jpg"': '"image": "assets/images/proj-6.png"',
    '"image": "assets/images/image18.jpg"': '"image": "assets/images/proj-7.png"',
    '"image": "assets/images/image19.jpg"': '"image": "assets/images/proj-8.png"',
    '"image": "assets/images/image21.jpg"': '"image": "assets/images/proj-9.png"',
    '"image": "assets/images/image23.jpg"': '"image": "assets/images/proj-10.png"',
    '"image": "assets/images/image24.jpg"': '"image": "assets/images/proj-11.png"',
    '"image": "assets/images/image25.jpg"': '"image": "assets/images/proj-12.png"',
    '"image": "assets/images/image26.jpg"': '"image": "assets/images/proj-13.png"',
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('build_final_dataset.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_final_dataset.py image paths!")
