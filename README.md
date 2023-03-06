# Batch Image Processor

This is a Python library that provides methods to **resize, crop, convert, rotate, and blur** images in a specified folder and its subfolders using the [Pillow](https://python-pillow.org/) (PIL Fork) library.

## Requirements

-   Python >=3.7
-   `typing` module
-   `os` module
-   `Pillow` (Pillow (PIL) Fork) >= 9.0.0

This package using **Pillow** library. Hence, it is **required** to install this package before installing batch image processing package. Please check the following documentation to install Pillow library

https://pillow.readthedocs.io/en/stable/

## Installation

You can simply intall this package by using `pip`

    pip install batch-image-processing

## Usage

Import the package to your file:

    from batch_image_processing import ImageProcessor
 
Create an object of `ImageProcessor` class. When you creating the instance, you need to pass two arguments.

 1. `path/to/image_folder`
 2. `path/to/output_folder`

`processor = ImageProcessor("images/images-to-crop", "images/processed-images")`

After that, call to the functions according to your preferences

**Resize Images**
   

     processor.resize_images(100, 100)

**Crop Images**

    processor.crop_images(50, 50, 150, 150)

**Convert images to another type**

    processor.convert_images("png")

**Rotate Images**

    processor.rotate_images(90)

**Blur Images**

    processor.blur_images(5)

**Grayscale Images**

    processor.grayscale_images()

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are  **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## Author

Author [Akash Manujaya](https://www.linkedin.com/in/akash-liyanaarachchi-425748174/)

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
