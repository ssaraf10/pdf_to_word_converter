import os
import tempfile
import img2pdf
from pdf2image import convert_from_path


def downscale_pdf(input_pdf_path, output_pdf_path, target_dpi=300, poppler_path=r"C:\poppler\Library\bin"):
    # Create a temporary directory to store intermediate images
    with tempfile.TemporaryDirectory() as temp_dir:
        # Convert PDF to images at target DPI
        images = convert_from_path(input_pdf_path, dpi=target_dpi, fmt='jpeg', output_folder=temp_dir, poppler_path=poppler_path)

        image_paths = []
        for i, img in enumerate(images):
            image_path = os.path.join(temp_dir, f"page_{i}.jpg")
            img.save(image_path, 'JPEG', quality=85)
            image_paths.append(image_path)

        # Convert the images back to a single PDF
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_paths))

    print(f"Downscaled PDF saved to: {output_pdf_path}")


# Example usage
input_pdf = r"C:\Users\sweth\OneDrive\Desktop\Swetha_passport_full scan_Apr2025.pdf"
output_pdf = r"C:\Users\sweth\OneDrive\Desktop\Swetha_passport_full scan_Apr2025_300dpi.pdf"
downscale_pdf(input_pdf, output_pdf)
