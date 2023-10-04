import PyPDF2


def decrypt_pdf(input_path, output_path, password):
    # Open the encrypted PDF file
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(password)

            # Create a new PDF writer object
            pdf_writer = PyPDF2.PdfWriter()

            # Add all the pages to the writer
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Write the decrypted content to a new PDF file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"Decryption successful. Saved to {output_path}")
        else:
            print("The PDF is not encrypted.")


# Replace these paths and password with your specific details
input_path = 'C:/Users/tharu/Downloads/JUL_2022.pdf'  # Input PDF path
output_path = 'C:/Users/tharu/Downloads/JULY_2022.pdf'  # Output PDF path
password = '1949533@07041999'  # PDF password

# Call the function to decrypt the PDF
decrypt_pdf(input_path, output_path, password)
