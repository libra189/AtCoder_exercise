# AtCoder実行環境

競技プログラミングを実行するための実行環境を構築

## 演習問題

[競技プログラミングの鉄則 演習問題 - AtCoder](https://atcoder.jp/contests/tessoku-book/tasks/)

## 環境構築

🚧WIP🚧

### 参考

[Pythonで始めるAtCoder環境構築【初心者向け】 - 3DCG school](https://3dcg-school.pro/python-atcoder-develop-environment/)

## 履修手順

`exercise`ディレクトリ以下で実行

1. 演習問題用ディレクトリの作成

    ```bash
    $ ./env.py setup a01
    ```

2. テストデータのダウンロード

    ```bash
    $ ./env dl a01 https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
    ```

3. プログラミング

    好きなエディタで作成 VSCodeのDev Containersがオススメ

4. テスト

    ```bash
    $ ./env.py test a01
    ```

5. 結果の確認

    ```bash
    $ ./env.py run a01
    ```
    ターミナルに実行結果が出力されるので、それらがACになっているかを確認する。もしWAやREになっているとスクリプトに間違いがあるので、修正する。

## online-judge-tool

### `online-judge-tools`とは

競技プログラミングを行う上で存在する典型作業を自動化するためのコマンド

[online-judge-tools - Github](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)

### コマンド

- テストデータのダウンロード
    ```bash
    $ oj d https://atcoder.jp/xxx
    ```

    例) A01 - The First Problemのテストデータをダウンロード
    ```bash
    $ oj d https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a
    ```

- テストの実行
    ```bash
    $ oj t -d test -c "python3 xxx.py"
    ```

## online-judge-template-generator

🚧WIP🚧　`online-judge-template-generator`を使う方法

[online-judge-tools/template-generator - Github](https://github.com/online-judge-tools/template-generator/blob/master/README.ja.md)
