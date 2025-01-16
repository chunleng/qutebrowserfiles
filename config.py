from qutebrowser.config.config import ConfigContainer
from qutebrowser.config.configfiles import ConfigAPI

from src import mapping, style

config: ConfigAPI = config  # pyright: ignore
c: ConfigContainer = c  # pyright: ignore

# https://www.qutebrowser.org/doc/help/settings.html
config.load_autoconfig()
c.url.default_page = "https://www.ecosia.org"
c.url.start_pages = [
    "https://app.todoist.com/app/today",
    "https://calendar.google.com/calendar",
    "https://mail.google.com/mail",
]
c.url.searchengines = {
    "DEFAULT": "https://www.ecosia.org/search?q={}",
    "docker": "https://hub.docker.com/search?q={}",
    "g": "https://www.google.com/search?q={}",
    "map": "https://www.google.com/maps/search/{}",
    "py": "https://pypi.org/search/?q={}",
    "rd": "https://docs.rs/{}",
    "rs": "https://docs.rs/releases/search?query={}",
    "yt": "https://www.youtube.com/results?search_query={}",
    ":": "http://127.0.0.1:{}",
}
c.completion.web_history.max_items = 10000

c.hints.chars = "aoeuhtns"
c.colors.webpage.darkmode.enabled = True
c.input.insert_mode.auto_load = True
c.input.insert_mode.auto_leave = False
c.input.insert_mode.leave_on_load = False
c.auto_save.session = True
c.confirm_quit = ["never"]
c.tabs.last_close = "close"
c.statusbar.widgets = ["url", "search_match", "progress"]

c.downloads.location.prompt = False
c.downloads.remove_finished = 10000
c.downloads.position = "bottom"
c.editor.command = [
    "/Applications/kitty.app/Contents/MacOS/kitty",
    "-1",
    "/bin/bash",
    "--login",
    "-c",
    "~/.asdf/shims/nvim +'setf browser' {file}",
]
c.content.pdfjs = True

mapping.setup(config)
style.setup(c)
