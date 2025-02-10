import glob
from os.path import expanduser
from pathlib import Path

from qutebrowser.config.config import ConfigContainer
from qutebrowser.config.configfiles import ConfigAPI
from qutebrowser.utils.urlmatch import UrlPattern

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
default_searchengine =  "https://www.ecosia.org/search?q={}"
c.url.searchengines = {
    "DEFAULT": default_searchengine,
    "docker": "https://hub.docker.com/search?q={}",
    "g": "https://www.google.com/search?q={}",
    "map": "https://www.google.com/maps/search/{}",
    "py": "https://pypi.org/search/?q={}",
    "rd": "https://docs.rs/{}",
    "rs": "https://docs.rs/releases/search?query={}",
    "s": default_searchengine,
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
c.content.headers._config.set_str(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:130.0) Gecko/20100101 Firefox/130",
    pattern=UrlPattern("https://accounts.google.com/*"),
)
c.colors.webpage.darkmode._config.set_str(
    "colors.webpage.darkmode.enabled",
    "false",
    pattern=UrlPattern("https://docs.google.com/*"),
)
c.scrolling.smooth = True
c.tabs.new_position.unrelated = "next"
c.content.headers.accept_language = "en;q=1,zh;q=0.9,jp;q=0.9"

mapping.setup(config)
style.setup(c)

# Configurations for local
home = expanduser("~")

bookmarks_files = glob.glob(f"{home}/.qutebrowser/bookmarks.*")
# Note when setting up the files for local, the last loaded key will be used for quickmarks if there is duplicate
quickmarks_files = glob.glob(f"{home}/.qutebrowser/quickmarks.*")

bookmarks_target = Path(f"{home}/.qutebrowser/bookmarks/urls")
quickmarks_target = Path(f"{home}/.qutebrowser/quickmarks")

with open(bookmarks_target, "a") as o:
    for f in bookmarks_files:
        with open(f, "r") as i:
            o.writelines(i.readlines())
with open(quickmarks_target, "a") as o:
    for f in quickmarks_files:
        with open(f, "r") as i:
            o.writelines(i.readlines())

try:
    import local

    local.setup(c, config)
except ModuleNotFoundError as e:
    # No local config
    pass
