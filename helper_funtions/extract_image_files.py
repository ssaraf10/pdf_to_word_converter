from pathlib import Path


def create_image_file_list(folder_path):
    img_file_lst = []
    for img_file in folder_path.rglob("*.png"):
        print(img_file)
        img_file_lst.append(img_file)

    return img_file_lst


def main():
    folder_path = Path(r"")

    img_file_lst = create_image_file_list(folder_path)
    print(img_file_lst)


if __name__ == "__main__":
    main()
