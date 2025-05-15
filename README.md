# Python QR Code Generator

A Python-based application for generating QR codes with a graphical user interface (GUI). This project enables users to convert text or URLs into QR codes, customize their appearance, and save them as image files.

## Features

- **Text to QR Code**: Convert any text or URL into a QR code.
- **Live Preview**: View the QR code as you type.
- **Custom Colors**: Choose different colors for the QR code.
- **Save Functionality**: Save QR codes as PNG or JPG files.
- **User-friendly Interface**: Easy-to-use GUI built with Python's `tkinter` library.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package manager)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/pattana1902/Python-QRCode-Generator.git
   cd Python-QRCode-Generator
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. Run the application:
  ```bash
   python qr_code_gui.py
   ```
2. Enter the text or URL you want to convert into a QR code.

3. Click the "Generate QR Code" button to display the QR code.

4. Use the "Save QR Code" button to save the generated QR code as an image file.

## Code Structure
- ```qr_code_gui.py```: Main application script that provides the GUI for QR code generation.
- Dependencies:
  - ```qrcode```: Library for generating QR codes.
  - ```Pillow```: Used for image manipulation and saving.
  - ```tkinter```: For creating the graphical user interface.
## Customization
You can customize the QR code generation by:

- Modifying the box_size and border parameters in the QR code generation code.
- Adding new color options for the QR code.
- Adjusting the GUI layout in the qr_code_gui.py file.

## Example
Application Interface  
![Application Interface](Application_Interface.png)

QR Code Preview  
![QR Code Preview](QR_Code_Preview.png)

## Contribution
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -m 'Add new feature').
4. Push your branch (git push origin feature-name).
5. Open a pull request.

## Acknowledgments

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/pattana1902/Python-QRCode-Generator/blob/master/LICENSE) file for more details.

## Acknowledgments

- [qrcode library](https://github.com/lincolnloop/python-qrcode) 
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)

##
Developed by [pattana1902](https://github.com/pattana1902) | © 2025 All Rights Reserved
