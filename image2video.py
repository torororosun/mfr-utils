import cv2
import os
import argparse

def main(folder_path, video_name, fps, width, height):

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # output file name, encoder, fps, size(fit to image size)
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    if not video.isOpened():
        print("can't be opened")
        sys.exit()


    file_list = sorted(os.listdir(folder_path))
    for file_name in file_list:
        image_path = os.path.join(folder_path, file_name)
        if not image_path.endswith('.jpg'):
            continue

        img = cv2.imread(image_path)

        if img is None:
            print("can't read")
            break

        video.write(img)

    video.release()
    print('written')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_path", type=str, help="画像が入っているフォルダパス、例：./output_data/")
    parser.add_argument("--video_name", type=str, help="動画の名前、例：./video.mp4")
    parser.add_argument("--fps", type=float, help="動画のフレームレート、例：10")
    parser.add_argument("--width", type=int, help="画像の横、例：400")
    parser.add_argument("--height", type=int, help="画像の縦、例：500")
    args = parser.parse_args()
    main(args.folder_path, args.video_name, args.fps, args.width, args.height)