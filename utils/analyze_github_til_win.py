from git import Repo
import os
import shutil
import aiofiles
import asyncio

"""github_collector window version"""

class AnalyzeGithubTil:
    def __init__(self, username, repository):
        self.username = username
        self.repository = repository
        self.results = []

    def clone_repositry(self):
        """Repository를 특정 디렉토리에 Clone 합니다."""
        Repo.clone_from(
            f"https://github.com/{self.username}/{self.repository}",
            f".anaylze\{self.username}\{self.repository}",
        )

    def get_markdown_file_path_list(self):
        """Clone한 레포지터리를 탐색하면서 md 파일 목록을 뽑아냅니다."""
        file_paths = []
        for top, _, files in os.walk(f".anaylze\{self.username}\{self.repository}"):
            for file_name in files:
                if file_name[-3:] == ".md":
                    file_paths.append([os.path.join(top, file_name), file_name])

        return file_paths

    async def get_file_content(self, path, file_name):
        """비동기로 파일을 읽어낸 후, 파일명과 파일 내용을 담아냅니다."""
        async with aiofiles.open(path, mode="r", encoding='utf-8') as f:
            content = await f.read()
            self.results.append([file_name[:-3], content])

    def perform(self):
        """메인 job 수행 메서드"""
        self.clone_repositry()
        path_list = self.get_markdown_file_path_list()

        tasks = set()
        for path, file_name in path_list:
            if file_name == "README.md" or file_name == "readme.md":    # readme 파일을 제외
                continue
            tasks.add(self.get_file_content(path, file_name))

        asyncio.run(asyncio.wait(tasks))

    def __del__(self):
        """작업을 마치면, 클론한 디렉토리를 제거합니다."""
        shutil.rmtree(f".anaylze\{self.username}\{self.repository}", ignore_errors=True)


if __name__ == "__main__":
    t = AnalyzeGithubTil("shinkeonkim", "TIL")
    t.perform()
    print(t.results)
