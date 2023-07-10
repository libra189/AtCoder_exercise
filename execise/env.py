#!/usr/local/bin/python3

import fire
import os
import shutil
import subprocess

class Cli(object):

    def __init__(self):
        self.template_dir = ".template"
        self.template_files = {
            "main": "main.py",
            "sample": "sample-1.in"
        }

    def setup(self, dir: str):
        """
        練習問題のディレクトリを作成

        @param dir(str): ディレクトリ名
        """
        os.makedirs(dir, exist_ok=True)
        shutil.copyfile(
            os.path.join(self.template_dir, self.template_files["main"]),
            os.path.join(dir, self.template_files["main"])
        )
        return f"Create the directory and template: {dir}."

    def dl(slef, dir: str, url: str):
        """
        練習問題をダウンロード

        @param dir(str): ディレクトリ名
        @param url(str): ダウンロードURL
        """
        cwd: str = os.getcwd()
        work_dir: str = os.path.join(cwd, dir)
        if not os.path.isdir(work_dir):
            self.setup(dir)

        os.chdir(work_dir)
        subprocess.run(["/usr/local/bin/oj", "d", url])
        os.chdir(cwd)

        return "Let's happy coding!"

    def test(self, dir: str):
        """
        sample-1.inのみテスト実行

        @param dir(str): ディレクトリ名
        """
        main_file = os.path.join(dir, self.template_files["main"])
        test_input = os.path.join(dir, "test", self.template_files["sample"])
        subprocess.run(f"/usr/local/bin/python3 {main_file} < {test_input}", shell=True)

    def run(self, dir: str):
        """
        演習問題の実行結果を確認

        @param dir(str): ディレクトリ名
        """
        cwd: str = os.getcwd()
        work_dir: str = os.path.join(cwd, dir)

        os.chdir(work_dir)
        subprocess.run(["/usr/local/bin/oj", "t", "-d", "test", "-c", f"python3 {self.template_files['main']}"])
        os.chdir(cwd)

if __name__ == "__main__":
    fire.Fire(Cli)
