import os
from pdf2image import convert_from_path

# Set the path to the PDF file
pdf_path = r'C:\Users\sweth\Downloads\IntroductionFromTheGreatRemobilization.pdf'

# Set the output directory for the image files
output_dir = r"C:\Users\sweth\Downloads\haas_berk_assignment"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Save each page as a separate image file
for i, image in enumerate(images):
    image_path = os.path.join(output_dir, f"page_{i+1}.jpg")
    image.save(image_path, "JPEG")

print(f"Saved {len(images)} image files to {output_dir}")
