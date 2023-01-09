import os
import sublime
import sublime_plugin
import subprocess


class GitOpenCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        filename = self.view.file_name()
        if filename is None:
            sublime.error_message("No Open File!")
            return

        directory = os.path.dirname(filename)

        self._run_open(directory, args.get("command", "repo"))

    def _run_open(self, directory, command):
        completed = subprocess.run(
            ['git', 'open', command],
            capture_output=True,
            cwd=directory
        )

        if completed.stdout != b'':
            print(bytes.decode(completed.stdout))

        if completed.returncode != 0:
            error = bytes.decode(completed.stderr)
            sublime.error_message(f'Error running git open.\n Error code: {completed.returncode}\n{error}')  # noqa: E501
