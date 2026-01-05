# robot_safety_system

![test](https://github.com/muuuuu2525/robot_safety_system2025/actions/workflows/test.yml/badge.svg)

* 距離センサーの値をシミュレートし、障害物が接近した場合に自動で緊急停止命令を出すROS 2パッケージです。

## ノードとトピックの構成

システムは以下の2つのノードと、それらを繋ぐトピックで構成されています。

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

## 概要

* **センサー機能**: 0.5m〜3.0mのランダムな距離データを定期的に生成・配信します。
* **判定機能**: 距離データを受信し、設定された閾値（1.0m）以下かどうかを判定します。
* **警告機能**: 距離が1.0mを下回った場合、ログレベルをWARN（警告）に引き上げて危険を知らせます。

## 実行環境

* Ubuntu 24.04 LTS / 22.04 LTS
* ROS 2 Jazzy Jalisco / Humble Hawksbill
* Python 3.10 ~ 3.12

## 使用方法

* ワークスペースでビルド後、以下のコマンドでシステム（センサーとブレーキ）を一括起動します。

```bash
ros2 launch robot_safety_system safety_system_launch.py
```

* 実行すると、以下のように距離に応じたログが出力されます。

## 通常
[sensor_simulator-1] [INFO]: Publishing distance: 2.45m
[safety_brake-2] [INFO]: Safe. Distance: 2.45m. GO.

## 接近検知
[sensor_simulator-1] [INFO]: Publishing distance: 0.85m
[safety_brake-2] [WARN]: DANGER! Distance: 0.85m. STOP!

#### ブロック3（ライセンス 〜 更新履歴）
```markdown
```

## ライセンス

* このパッケージは、Apache-2.0 Licenseの下で公開されています。
* © 2025 Taro Chiba 







