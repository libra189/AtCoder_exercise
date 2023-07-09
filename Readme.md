# AtCoder実行環境

競技プログラミングを実行するための実行環境を構築

## 演習問題

[競技プログラミングの鉄則 演習問題 - AtCoder](https://atcoder.jp/contests/tessoku-book/tasks/)

## 環境構築

🚧WIP🚧

### 参考

[Pythonで始めるAtCoder環境構築【初心者向け】 - 3DCG school](https://3dcg-school.pro/python-atcoder-develop-environment/)

## コマンド

- テストデータのダウンロード
    ```bash
    $ oj d https://atcoder.jp/contests/tessoku-book/tasks/xxx
    ```

    例) A01 - The First Problemのテストデータをダウンロード
    ```bash
    $ oj d https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
    ```

- テストの実行
    ```bash
    $ oj t -d test -c "python3 xxx.py"
    ```

## 履修手順

1. 演習問題用ディレクトリの作成
    ```bash
    $ mkdir execise/a01
    ```
2. テストデータのダウンロード
    ```bash
    $ cd execise/a01
    $ oj d https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
    ```
3. プログラミング

    好きなエディタで作成 VSCodeのDev Containersがオススメ
4. テスト
    ```bash
    $ oj t -d test -c "python3 main.py"
    ```
    ターミナルに実行結果が出力されるので、それらがACになっているかを確認する。もしWAやREになっているとスクリプトに間違いがあるので、修正する。
