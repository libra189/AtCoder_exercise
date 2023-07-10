import fire
import os
import shutil

class Cli(object):

    def __init__(self):
        self.template_dir = ".template"
        self.template_files = {
            "main": "main.py"
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
        return f"Create the directory: {dir}.\nLet's happy coding."

    def hello(self):
        return "Hello world."

if __name__ == "__main__":
    fire.Fire(Cli)
