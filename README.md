# mfr-utils

## レポジトリについて

stable diffusion WebUIのmulti-frame renderingで、動画を生成する時に使っているpython scriptsです。

自分はなんとなくこれらを使っているのですが、WebUIのextentionや、アプリで代替できるかもしれないです。

## スクリプトの説明

### video2image.py

img2imgに入れる画像を作るために、動画を細切れの画像に変換する。

この処理を代替できるアプリケーションは[aviutl](http://spring-fragrance.mints.ne.jp/aviutl/)とか。

コマンドライン例
```
python ./video2image.py --video_path ./video.mp4 --output_dir ./train_data --img_prefix image --img_extension png --skip_fps 10
```

### delete_tags.py

DeepDanbooruで作成したタグから、不必要なタグを削除する。

本家のREADMEを全部は読めてないのですが、コマンドラインでもしかしたらこのタグを生成しないみたいな制御はできるかもしれないです。

コマンドライン例
```
python ./delete_tags.py --folder_path ./train_data --delete_tags "1girl,white_shirt"
```

### image2video.py

multi-frame renderingで生成した画像をくっつけて動画にする。

この処理を代替できるアプリケーションは[GIFアニメーション画像作成ツール](https://photocombine.net/gifanime/)とか。


コマンドライン例
```
python ./image2video.py --folder_path ./output_data --video_name ./video.mp4 --fps 10.0 --width 432 --height 768
```