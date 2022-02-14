from git import Repo
from pydriller import Repository
import os
import shutil
import aiofiles
import asyncio

"""github_collector mac version"""


class AnalyzeGithubTil:
    def __init__(self, username, repository):
        self.username = username
        self.repository = repository
        self.results = []
        self.dates_by_file = {}

    def clone_repositry(self):
        """Repository를 특정 디렉토리에 Clone 합니다."""
        try:
            Repo.clone_from(
                f"https://github.com/{self.username}/{self.repository}",
                f"./analyze/{self.username}/{self.repository}",
            )
            return True
        except:
            return False

    def get_markdown_file_path_list(self):
        """Clone한 레포지터리를 탐색하면서 md 파일 목록을 뽑아냅니다."""
        file_paths = []
        for top, _, files in os.walk(f"./analyze/{self.username}/{self.repository}"):
            for file_name in files:
                if file_name[-3:].lower() == ".md":
                    file_paths.append([os.path.join(top, file_name), file_name])

        return file_paths

    async def get_file_content(self, path, file_name):
        """비동기로 파일을 읽어낸 후, 파일명과 파일 내용을 담아냅니다."""
        async with aiofiles.open(path, mode="r") as f:
            content = await f.read()
            self.results.append([file_name[:-3], content, path])

    def get_date(self):
        """파일의 생성일자, 수정일자 딕셔너리"""
        for commit in Repository(
            f"https://github.com/{self.username}/{self.repository}"
        ).traverse_commits():
            file_date = str(commit.committer_date)

            for file in commit.modified_files:
                file_path = file.new_path or file.old_path

                if (
                    file.filename == "README.md" or file.filename == "readme.md"
                ):  # readme 파일을 제외
                    continue

                if file.filename[-3:].lower() != ".md":
                    continue

                if file_path in self.dates_by_file:
                    self.dates_by_file[file_path].append(file_date)
                    continue

                self.dates_by_file[file_path] = [file_date]

    def perform(self):
        """메인 job 수행 메서드"""
        try:
            is_cloned = self.clone_repositry()
            if not is_cloned:
                return

            path_list = self.get_markdown_file_path_list()

            self.get_date()

            tasks = set()
            for path, file_name in path_list:
                if (
                    file_name == "README.md" or file_name == "readme.md"
                ):  # readme 파일을 제외
                    continue
                tasks.add(self.get_file_content(path, file_name))

            asyncio.run(asyncio.wait(tasks))
        except Exception as e:
            print(e)
            return

    def __del__(self):
        """작업을 마치면, 클론한 디렉토리를 제거합니다."""
        shutil.rmtree(f"./analyze/{self.username}/{self.repository}")


if __name__ == "__main__":
    t = AnalyzeGithubTil("shinkeonkim", "TIL")
    t.perform()
    print(t.results)
    print(t.dates_by_file)
