# robot_safety_system

[![test](https://github.com/muuuuu2525/robot_safety_system/actions/workflows/test.yml/badge.svg)](https://github.com/muuuuu2525/robot_safety_system/actions/workflows/test.yml)

* 距離センサーの値をシミュレートし、障害物が接近した場合に自動で緊急停止命令を出すROS 2パッケージです。

## ノードとトピックの構成

システムは以下の2つのノードと、それらを繋ぐトピックで構成されています。

### ノード一覧

| ノード名 | 役割 | ソースファイル |
| :--- | :--- | :--- |
| `sensor_simulator` | 距離センサーの値を模倣し、定期的にデータを送信します。 | `sensor_simulator.py` |
| `safety_brake` | 距離データを受信し、危険な距離（1.0m未満）なら停止命令を出します。 | `safety_brake.py` |

### トピック一覧

| トピック名 | データ型 | パブリッシャ | サブスクライバ | 説明 |
| :--- | :--- | :--- | :--- | :--- |
| `/distance` | `std_msgs/Float32` | `sensor_simulator` | `safety_brake` | センサーが計測した障害物までの距離 |
| `/safety_status` | `std_msgs/String` | `safety_brake` | - (外部監視用) | 安全状態を示すステータス（"GO" / "STOP"） |

## 概要

* **センサー機能**: 0.5m〜3.0mのランダムな距離データを定期的に生成・配信します。
* **判定機能**: 距離データを受信し、設定された閾値（1.0m）以下かどうかを判定します。
* **警告機能**: 距離が1.0mを下回った場合、ログレベルをWARN（警告）に引き上げて危険を知らせます。

## 実行環境

* Ubuntu 24.04 LTS / 22.04 LTS
* ROS 2 Jazzy Jalisco / Humble Hawksbill
* Python 3.10 ~ 3.12

## 実行・動作確認

## システムの起動
   動作確認を行うため、以下のコマンドでビルドと起動を実行します。
   ```bash
   ros2 launch robot_safety_system safety_system_launch.py
   ```

## トピック通信の確認 
   別のターミナルを開き、以下のコマンドでノード間の通信状況（データ）を直接確認できます。

* 距離データ

```bash
$ ros2 topic echo /distance
data: 2.45
---
data: 0.85
---
```

* 出力例:

```YAML
data: 2.45
---
data: 0.85
---
```

* 安全ステータス

```bash
$ ros2 topic echo /safety_status
data: "GO"
---
data: "STOP"
---
```

* 出力例:

```YAML
data: "GO"
---
data: "STOP"
---
```

## ライセンス

* このパッケージは、Apache-2.0 Licenseの下で公開されています。
* © 2025 Manamu Asano 







