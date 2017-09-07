# coding: utf-8

import datetime
import sqlite3handler

# spi, time ライブラリをインポート
import spidev
import time

# SpiDev オブジェクトのインスタンスを生成
spi = spidev.SpiDev()

# ポート0、デバイス0のSPI をオープン
spi.open(0, 0)

# 最大クロックスピードを1MHz に設定
spi.max_speed_hz=1000000

# 1 ワードあたり8ビットに設定
spi.bits_per_word=8

# ダミーデータを設定（1111 1111）
dummy = 0xff

# スタートビットを設定（0100 0111）
start = 0x47

# シングルエンドモードを設定 （0010 0000）
sgl = 0x20

# ch0 を選択（0000 0000）
ch0 = 0x00

# MSB ファーストモードを選択（0000 1000）
msbf = 0x08

# IC からデータを取得する関数を定義
def measure(ch):
    # SPI インターフェイスでデータの送受信を行う
    ad = spi.xfer2( [ (start + sgl + ch + msbf), dummy ] )
    #
    val = ((ad[0] & 0x03) << 8) + ad[1] 
    # 受信した2バイトのデータを10 ビットデータにまとめる
    voltage =  ( val * 3.3 ) / 1023
    # 結果を返す
    return val, voltage

# 例外を検出
try:
    # 書き込むレコードをまとめる数
    N  = 6
    # 平均を取る計測データ数
    M  = 10
    # 計測頻度
    dt = 1
    # 無限ループ
    while True:
        # 関数を呼び出してch0 のデータを取得
        #ch0_val, ch0_voltage  = measure(ch0)
        # 結果を表示
        #print('ch0 = {:4d}, {:2.2f}[V]'.format(ch0_val, ch0_voltage))
        # 1分毎に書き込み
        data = []
        for j in range(N):
            # 10 秒毎に平均
            ch0_val = ch0_voltage = 0
            for i in range(M):
                val, vol = measure(ch0)
                ch0_val     += val
                ch0_voltage += vol
                #print(val, vol)
                time.sleep(dt)
            data.append((datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), ch0_val/M, ch0_voltage/M))
            #print(data)
        db = sqlite3handler.sqlite3handler('data.db')
        db.insert_data('light', data)
        del(db)

# キーボード例外を検出
except KeyboardInterrupt:
    # 何も処理をしない
    pass

# SPI を開放
spi.close()
