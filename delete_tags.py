import os
import argparse

def main(folder_path, delete_tags):
    if os.path.isdir(folder_path):
        print(f"folder path: {folder_path}")
    else:
        print(f"invalid folder path: {folder_path}")

    delete_tags = delete_tags.split(',')

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"): # テキストファイルのみ処理する
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            for delete_tag in delete_tags:
                content = content.replace(delete_tag, '')
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, help="画像が入っているフォルダパス、例：./train_data/")
    parser.add_argument("--delete_tags", type=str, help="消したいタグ集、例：read_hair,1girl")
    args = parser.parse_args()
    main(args.folder_path, args.delete_tags)
