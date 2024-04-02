from io import BytesIO
from pathlib import Path
from img2pdf import convert
from PIL import Image
from helper_funtions.extract_image_files import create_image_file_list


folder_path = Path(r"")
image_paths = create_image_file_list(folder_path)

images_bytes = []
for path in image_paths:
    with Image.open(path) as img:
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")  # Save image as PNG bytes
        images_bytes.append(img_bytes.getvalue())

# Generate the PDF
pdf_bytes = convert(images_bytes)

# Save the PDF
with open(r"", "wb") as f:
    f.write(pdf_bytes)

print("PDF created")
