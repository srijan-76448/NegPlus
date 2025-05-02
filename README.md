# NegPlus
NegPlus (**Neg+**) is a CLI based tool using which anybody can convert any Negetive image into a Black &amp; White picture or a color picture.

## Functionality
NegPlus allows you to process image files using various color scales:
- **Grayscale:** Converts the image to black and white.
- **Red:** Extracts only the red channel of the image.
- **Green:** Extracts only the green channel of the image.
- **Blue:** Extracts only the blue channel of the image.
- **Negative:** Inverts the colors of the image.
- **All:** Processes the image with all the above scales, generating separate output files.

## Usage
```bash
python3 main.py <scale> <image_path> [output_path]
```
- `<scale>`: Specifies the desired image transformation. Available options are `-bw`, `-r`, `-g`, `-b`, `-ng`, and `-all`.
- `<image_path>`: The path to the input image file.
- `[output_path]` (optional): The path where the processed image will be saved. If not provided, the output image will be saved in the same directory as the input image, with the scale appended to the filename (e.g., `image-BW.png`).

## Options
| Option | Description                                    |
| :----- | :--------------------------------------------- |
| `-bw`  | Returns the grayscale image.                   |
| `-r`   | Returns the red portion of the image only.     |
| `-g`   | Returns the green portion of the image only.   |
| `-b`   | Returns the blue portion of the image only.    |
| `-ng`  | Returns the negative of the image.             |
| `-all` | Processes the image with all available scales. |

## Dependencies
- Python 3
- [Pillow](https://pypi.org/project/pillow/)
