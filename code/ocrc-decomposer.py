import fitz  # PyMuPDF
import argparse

def extract_text_and_images(pdf_path, output_folder):
    """
    Extracts text and images from each page of an OCR PDF.
    Saves images as PNG files in `output_image_folder`.
    Returns a list of extracted texts (one entry per page).
    """
    import os

    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    doc = fitz.open(pdf_path)
    texts = []

    with open(f"{output_folder}/output_text.txt", "w", encoding="utf-8") as file:
        for page_index in range(len(doc)):
            page = doc[page_index]

            # ---- 1) Extract Text -------------------------------------
            page_text = page.get_text()  
            # Or page.get_text("text") for raw text extraction
            # (In most cases, page.get_text() will suffice.)
            texts.append(page_text)
            file.write(page_text)

            # ---- 2) Extract Images -----------------------------------
            image_list = page.get_images(full=True)
            for img_index, img_info in enumerate(image_list, start=1):
                xref = img_info[0]  # the XREF of the image
                # Generate a Pixmap from the image
                pix = fitz.Pixmap(doc, xref)

                # Check if image is grayscale or RGB
                if pix.n < 5:  # this means GRAY or RGB
                    pix.save(f"{output_folder}/page{page_index}_img{img_index}.png")
                else:
                    # CMYK or other more complex color formats need conversion
                    pix_converted = fitz.Pixmap(fitz.csRGB, pix)
                    pix_converted.save(f"{output_folder}/page{page_index}_img{img_index}.png")
                    pix_converted = None
                
                pix = None  # free resources

    doc.close()
    # with open(f"{output_folder}/output.txt", "w", encoding="utf-8") as file:

def main():
    parser = argparse.ArgumentParser(
        description="Extract text and images from an OCRed PDF."
    )
    # Define command-line arguments:
    parser.add_argument(
        "--pdf", 
        type=str, 
        required=True, 
        help="Path to the PDF file."
    )
    parser.add_argument(
        "--out", 
        type=str, 
        default="output", 
        help="Output folder for extracted txt and images files (default: the name of the pdf file)."
    )

    args = parser.parse_args()
    pdf_file = args.pdf
    out_folder = ""
    if args.out is not None:
        out_folder = args.out
    else:
        out_folder = args.pdf[0]

    extract_text_and_images(pdf_file, out_folder)

if __name__ == "__main__":
    main()