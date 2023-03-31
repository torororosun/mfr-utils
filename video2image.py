import cv2
import os
import argparse

def main(video_path, output_dir, img_prefix, img_extension, skip_fps):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)

    frame_num = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_num % skip_fps == 0:
            img_file_name = f"{img_prefix}{frame_num:04d}.{img_extension}"
            img_file_path = os.path.join(output_dir, img_file_name)

            cv2.imwrite(img_file_path, frame)

        frame_num += 1

    cap.release()

    print(f"{frame_num} frames extracted and saved to {output_dir}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, help="動画ファイルのパス、例：./video.mp4")
    parser.add_argument("--output_dir", type=str, help="画像ファイルを保存するディレクトリ、例：./output")
    parser.add_argument("--img_prefix", type=str, help="画像ファイル名のprefix、例：image_")
    parser.add_argument("--img_extension", type=str, help="画像ファイルの拡張子、例：png")
    parser.add_argument("--skip_fps", type=int, help="スキップするフレーム数、例：10")
    args = parser.parse_args()
    main(args.video_path, args.output_dir, args.img_prefix, args.img_extension, args.skip_fps)