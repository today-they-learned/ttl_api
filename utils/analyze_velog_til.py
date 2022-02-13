import subprocess


class AnalyzeVelogTIL:
    def __init__(self, username):
        self.username = username
        self.results = []

    def perform(self):
        proc = subprocess.Popen(
            ["node", "utils/velog-backup/app.js", "-u", self.username],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            universal_newlines=True,
            text=True,
        )

        ret, err = proc.communicate()

        print(err)

        for post in ret.split("&&&&&&end------"):
            post_content = post.split("!@#$%^&*(!*!&@%!$@!&*@%!@$!")[:-1]

            if len(post_content) != 4:
                continue

            title, body, tags, released_at = post_content

            result = {
                "title": title.strip(),
                "body": body.strip(),
                "tags": tags.strip().split(","),
                "released_at": released_at.strip(),
            }
            self.results.append(result)


if __name__ == "__main__":
    t = AnalyzeVelogTIL("singun11")
    t.perform()

    print(t.results)
