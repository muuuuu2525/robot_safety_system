# robot_safety_system

![test](https://github.com/muuuuu2525/robot_safety_system2025/actions/workflows/test.yml/badge.svg)

* 距離センサーの値をシミュレートし、障害物が接近した場合に自動で緊急停止命令を出すROS 2パッケージです。

## 概要

* **センサー機能**: 0.5m〜3.0mのランダムな距離データを定期的に生成・配信します。
* **判定機能**: 距離データを受信し、設定された閾値（1.0m）以下かどうかを判定します。
* **通信機能**: `/distance` トピックで距離を、`/safety_status` トピックで安全状態（GO/STOP）を配信します。
* **警告機能**: 距離が1.0mを下回った場合、ログレベルをWARN（警告）に引き上げて危険を知らせます。

## 実行環境

* Ubuntu 24.04 LTS / Ubuntu 22.04 LTS
* ROS 2 Jazzy Jalisco / Humble Hawksbill
* Python 3.10 ~ 3.12

## 必要なライブラリ / 必要なパッケージ

* ROS 2の標準ライブラリ（`rclpy`, `std_msgs`）のみを使用しているため、追加のインストールは不要です。

## セットアップ

* 以下のコマンドでリポジトリをクローンし、ビルドします。

```bash
cd ~/ros2_ws/src
git clone [https://github.com/muuuuu2525/robot_safety_system2025.git](https://github.com/muuuuu2525/robot_safety_system2025.git)
cd ~/ros2_ws
colcon build --packages-select robot_safety_system
```

## 使用方法
* 以下のコマンドを実行して、システム（センサーとブレーキ）を起動します。

```bash
source install/setup.bash
ros2 launch robot_safety_system safety_system_launch.py
```

* 実行すると、以下のように距離に応じたログが出力されます。

## 安全な距離
[sensor_simulator-1] [INFO] [1735540000.123456789] [sensor_simulator]: Publishing distance: 2.45m
[safety_brake-2] [INFO] [1735540000.124567890] [safety_brake]: Safe. Distance: 2.45m. GO.

* 障害物が接近（1.0m未満）すると、以下のように警告（WARN）が表示され、停止命令が出ます。

## 接近検知
[sensor_simulator-1] [INFO] [1735540005.987654321] [sensor_simulator]: Publishing distance: 0.85m
[safety_brake-2] [WARN] [1735540005.988765432] [safety_brake]: DANGER! Distance: 0.85m. STOP!

## ライセンス
* このパッケージは、Apache-2.0 Licenseの下で公開されています。
* © 2025 Taro Chiba EOF




























## ノードとトピックの構成

このシステムは以下の2つのノードと、それらを繋ぐトピックで構成されています。

### ノード一覧

| ノード名 | 役割 | ソースファイル |
| :--- | :--- | :--- |
| `sensor_simulator` | 距離センサーの値を模倣し、定期的にデータを送信します。 | `sensor_simulator.py` |
| `safety_brake` | 距離データを受信し、危険な距離（1.0m未満）なら停止命令を出します。 | `safety_brake.py` |

### トピック一覧

| トピック名 | データ型 | 通信方向 | 説明 |
| :--- | :--- | :--- | :--- |
| `/distance` | `std_msgs/Float32` | `sensor` → `brake` | センサーが計測した障害物までの距離（メートル） |
| `/safety_status` | `std_msgs/String` | `brake` → 外部 | 安全状態を示すステータス（"GO" または "STOP"） |
