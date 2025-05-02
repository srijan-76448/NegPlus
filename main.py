from PIL import Image
import os, sys


scales = {
    "-r": "red",
    "-g": "green",
    "-b": "blue",
    "-bw": "grey",
    "-ng": "negetive",
    # "-in": "inverted",
    "-all": "all"
}


def converter(image_path, scale, format: str = 'PNG', output_path: str = None):
    img = Image.open(image_path)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            px = (r, g, b)

            if scale == "grey":
                px = (int(sum([r, g, b])/3), int(sum([r, g, b])/3), int(sum([r, g, b])/3))
                
            if scale == "negetive":
                px = (255-r, 255-g, 255-b)

            if scale == "red":
                px = (r, 0, 0)

            if scale == "green":
                px = (0, g, 0)

            if scale == "blue":
                px = (0, 0, b)

            if scale == "inverted":
                px = (b, g, r)

            pixels[x, y] = px

    if output_path is None:
        img_dir  = os.path.split(image_path)[0]
        img_name = os.path.split(image_path)[1].split(".")[0]
        img_scle = scale.upper()
        img_extn = format.lower()
        output_path = os.path.join(img_dir, f"{img_name}-{img_scle}.{img_extn}")

    img.save(output_path, format=format)
    print(f"\033[92;1m[+] \033[0mImage successfully processed and saved to: \033[1m{output_path}\033[0m")


def help():
    print("""Usage: python main.py <scale> <image_path> [output_path]

Options             Description
-bw                 Returns the grayscale image
-r                  Returns the red portion of the image only
-g                  Returns the green portion of the image only
-b                  Returns the blue portion of the image only
-ng                 Returns the negetive of the image
-in                 Returns the image inter changing the RGB value as BGR
""")
    exit()


def main():
    args = sys.argv[1:]
    flag = [i for i in args if i[0] == "-"][0]
    args.remove(flag)
    args = [i for i in args if i[0] != "-"]

    if len(args) == 0:
        help()

    if flag not in scales:
        print(f"\033[91;1m[-] Error:\033[0m Invalid scale '\033[1m{flag}\033[0m'.\n")
        help()

    input_image = args[0]
    opt_img = args[1] if len(args) > 1 else None
    scale = scales[flag]
    
    if not os.path.exists(input_image):
        print(f"\033[91;1m[-] Error:\033[0m Image not found at '\033[1m{input_image}\033[0m'.")
        exit()

    if flag == "-all":
        for scale in scales.values():
            if scale != "all":
                converter(input_image, scale, output_path=opt_img)

    else:
        converter(input_image, scale, output_path=opt_img)


if __name__ == "__main__":
    main()
