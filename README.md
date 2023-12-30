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
* サブスクライバを持つノード. トピック`/random_numbers`から1~100のランダムな整数10個を受信し,素数を選ぶ問題を出力し,その後30秒後に答えを出力する.

### randam_number_ans.py
* randam_number.pyとprime_ans.pyを同時に起動する.

## 実行手順
### talkerとlistener
* `ros2 run`実行方法
```bash
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
```
実行後, 下記のように出力される. 終了は`Ctrl+C`をする.
```bash
[INFO] [1703921013.808205462] [listener]: Listen: 0
[INFO] [1703921014.300763156] [listener]: Listen: 1
[INFO] [1703921014.800532393] [listener]: Listen: 2
[INFO] [1703921015.301099035] [listener]: Listen: 3
[INFO] [1703921015.800944378] [listener]: Listen: 4
[INFO] [1703921016.300543882] [listener]: Listen: 5
[INFO] [1703921016.800654606] [listener]: Listen: 6
                         .
                         .
```
* `ros2 launch`実行方法
```
$ ros2 launch mypkg talk_listen.launch.py
```
実行後, 下記のように出力される. 終了は`Ctrl+C`をする.
```bash
[INFO] [launch]: All log files can be found below /home/ragi/.ros/log/2023-12-30-16-27-11-280534-RyoPC-13268
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [13270]
[INFO] [listener-2]: process started with pid [13272]
[listener-2] [INFO] [1703921232.204231986] [listener]: Listen: 0
[listener-2] [INFO] [1703921232.693374241] [listener]: Listen: 1
[listener-2] [INFO] [1703921233.193636850] [listener]: Listen: 2
[listener-2] [INFO] [1703921233.693465548] [listener]: Listen: 3
[listener-2] [INFO] [1703921234.193672292] [listener]: Listen: 4
[listener-2] [INFO] [1703921234.693433063] [listener]: Listen: 5
[listener-2] [INFO] [1703921235.193450279] [listener]: Listen: 6
                         .
                         .
```
### randam_number.pyとprime_ans.py
* `ros2 run`実行方法
```bash
端末1$ ros2 run mypkg prime_ans
端末2$ ros2 run mypkg randam_number
```
実行後, 下記のような問題が出力される.実行後すぐに問題が出力されない場合もあり,その場合30秒後に問題が出力される.
```bash
[INFO] [1703922289.513912013] [random_ans]: Select a prime number from the following list:
[INFO] [1703922289.514429083] [random_ans]: [74, 79, 9, 22, 71, 43, 53, 17, 85, 93]
```
問題出力30秒後に下記ような答えが出力される.終了は`Ctrl+C`をする.問題から素数がどれかを考えよう.
```bash
[INFO] [1703922318.981318353] [random_ans]: Time up! The answer is:
[INFO] [1703922318.981896856] [random_ans]: [79, 71, 43, 53, 17]
```

## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 20.04
* ROS2 foxy

## 著作権・ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
   * [ryuichiueda/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
   * [ryuichiueda/my_slides/robosys_2022/lesson11](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson11.html#/)  
* © 2023 Ryohei Tsuchida
