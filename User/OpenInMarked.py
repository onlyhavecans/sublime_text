import subprocess
import sublime
import sublime_plugin


class OpenInMarkedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if filename is None:
            sublime.error_message("Save file before opening in Marked")
            return

        try:
            subprocess.check_call(['open', '-a', 'Marked 2', filename])
        except subprocess.CalledProcessError as e:
            sublime.error_message(f'Unable to open with Marked 2: {e}')
