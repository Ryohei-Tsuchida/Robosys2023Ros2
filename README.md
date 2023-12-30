# mypkg


ROS 2 のパッケージ

## リポジトリ内のノード,ファイル一覧

### talker.py
* パブリッシャを持つノード. 数字をカウントしてトピック`/countup`を通じて送信する.
   * トピックに流れるメッセージの型は16ビットの符号付き整数.
  
### listener.py
* サブスクライバを持つノード. トピック`/countup`からメッセージを受信し表示する

### talk_listen.launch.py
* talker.pyとlistener.pyを同時に起動する.

### randam_number.py
* パブリッシャを持つノード. 1~100のランダムな整数10個を`/random_numbers`を通じて送信する.
   * トピックに流れるメッセージの型は32ビットの符号付き整数の配列.

### prime_ans.py
* サブスクライバを持つノード. トピック`/random_numbers`から1~100のランダムな整数10個を受け取り, 

## 実行手順
### talkerとlistener
* `ros2 run`で実行する方法
```bash
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
[INFO] [1701248203.389102109] [listener]: Listen: 0
[INFO] [1701248203.871938229] [listener]: Listen: 1
[INFO] [1701248204.372729350] [listener]: Listen: 2
[INFO] [1701248204.872113956] [listener]: Listen: 3
[INFO] [1701248205.373301079] [listener]: Listen: 4
[INFO] [1701248205.872914002] [listener]: Listen: 5
                         .
                         .
                         .
```
実行後, 上記のように出力される. 終了するときは`Ctrl+C`

* `ros2 launch`で実行する方法
```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/shiozawa/.ros/log/2023-11-30-03-00-30-886468-shiopc-14400
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [14402]
[INFO] [listener-2]: process started with pid [14404]
[listener-2] [INFO] [1701280831.771362748] [listener]: Listen: 0
[listener-2] [INFO] [1701280832.253171938] [listener]: Listen: 1
[listener-2] [INFO] [1701280832.753223990] [listener]: Listen: 2
[listener-2] [INFO] [1701280833.252446603] [listener]: Listen: 3
[listener-2] [INFO] [1701280833.752907282] [listener]: Listen: 4
[listener-2] [INFO] [1701280834.253602883] [listener]: Listen: 5
                         .
                         .
                         .
```
実行後, 上記のように出力される. 終了するときは`Ctrl+C`

