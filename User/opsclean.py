import sublime_plugin


class OpsCleanCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        links = self.view.find_all(r" \(.+\)$")
        for link in reversed(links):
            self.view.erase(edit, link)

        headers = self.view.find_all(r"^\*")
        for header in reversed(headers):
            self.view.replace(edit, header, "###")
