from qutebrowser.config.configfiles import ConfigAPI # type: ignore
from qutebrowser.config.config import ConfigContainer # type: ignore
config: ConfigAPI = config
c: ConfigContainer = c

config.load_autoconfig(False)


c.input.insert_mode.auto_load = True
c.tabs.background = False

c.hints.chars = 'aoeuhtns' # dvorak home keys
c.url.default_page = "https://www.google.com"
c.url.start_pages = ["https://todoist.com/app/today"]
c.url.searchengines = {
    'DEFAULT':  'https://google.com/search?hl=en&q={}',
    '!a':       'https://www.amazon.com/s?k={}',
    '!d':       'https://thefreedictionary.com/{}',
    '!i':       'https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1',
    '!m':       'https://www.google.com/maps/search/{}',
    '!r':       'https://www.reddit.com/search?q={}',
    '!w':       'https://en.wikipedia.org/wiki/{}',
    '!y':       'https://www.youtube.com/results?search_query={}'
}
c.completion.open_categories = ["quickmarks", "bookmarks", "history", "filesystem", "searchengines"]
c.confirm_quit = ["multiple-tabs", "downloads"]
c.tabs.last_close = 'close'

# Look and feel
c.tabs.favicons.scale = 1.2
c.scrolling.bar = 'always'
c.tabs.position = 'bottom'
c.downloads.position = 'bottom'
c.tabs.max_width = 250
c.colors.tabs.bar.bg = '#1d1f21'
c.colors.statusbar.normal.bg = '#1d1f21'
c.colors.statusbar.normal.fg = '#e0e0e0'
c.colors.statusbar.command.bg = '#282a2e'
c.colors.statusbar.command.fg = '#e0e0e0'
c.colors.downloads.bar.bg = '#1d1f21'
c.fonts.default_size = "14pt"
c.fonts.tabs.selected = "bold default_size default_family"

c.colors.tabs.pinned.odd.bg = '#233443'
c.colors.tabs.pinned.odd.fg = '#969896'
c.colors.tabs.pinned.even.bg = '#233443'
c.colors.tabs.pinned.even.fg = '#969896'
c.colors.tabs.odd.bg = '#1d1f21'
c.colors.tabs.odd.fg = '#969896'
c.colors.tabs.even.bg = '#1d1f21'
c.colors.tabs.even.fg = '#969896'
c.colors.tabs.selected.even.bg = '#456887'
c.colors.tabs.selected.odd.bg = '#456887'
c.colors.tabs.pinned.selected.even.bg = '#456887'
c.colors.tabs.pinned.selected.odd.bg = '#456887'
c.colors.statusbar.insert.bg = '#b5bd68'
c.colors.statusbar.insert.fg = '#1d1f21'

c.fonts.messages.error = "default_size default_family"
c.colors.messages.error.bg = "#cc6666"
c.colors.messages.error.fg = "#ffffff"
c.colors.messages.error.border = "#cc6666"
c.colors.messages.info.bg = "#cc6666"

c.fonts.default_family = 'Arial'
c.fonts.statusbar = '12pt Hack Nerd Font'
c.colors.webpage.bg = '#ffffff' # prevent flashing when page load
c.colors.webpage.preferred_color_scheme = 'dark'
c.window.title_format = '{current_url}'
c.statusbar.widgets = ['progress', 'history']

c.tabs.padding = {"bottom": 7, "left": 7, "right": 7, "top": 7}
c.statusbar.padding = {"bottom": 3, "left": 10, "right": 10, "top": 15}

c.completion.height = '30%'

# don't hide decoration due to resize bug:
# https://github.com/qutebrowser/qutebrowser/issues/4067
# c.window.hide_decoration = True

# Keybindings
b = config.bind
def b_all(key, cmd):
    b(key, cmd, mode='normal')
    b(key, cmd, mode='insert')
    b(key, cmd, mode='hint')
    b(key, cmd, mode='passthrough')
    b(key, cmd, mode='command')
    b(key, cmd, mode='prompt')
    b(key, cmd, mode='yesno')
    b(key, cmd, mode='register')

b_all('<ctrl-cmd-n>', 'tab-next')
b_all('<ctrl-cmd-p>', 'tab-prev')
b('<ctrl-o>', 'back')
b('<ctrl-i>', 'forward')
b('H', 'tab-move -')
b('L', 'tab-move +')
b('gp', 'tab-pin')
b('<space>bl', 'tab-only --prev --pinned keep')
b('<space>bh', 'tab-only --next --pinned keep')
b_all('<cmd-w>', 'tab-close')
b('<ctrl-x>', 'tab-close')
b('<space>x', 'close')
b('O', 'set-cmd-text :open {url}')
b('t', 'set-cmd-text --space :open -t')
b('T', 'set-cmd-text :open -t {url}')
b('<esc>', 'fake-key <esc>')
b_all('<cmd-q>', 'quit --save')
b_all('<cmd-t>', 'open -t')
b('<ctrl-n>', 'fake-key <down>', mode='insert')
b('<ctrl-p>', 'fake-key <up>', mode='insert')
b('p', 'open -- {clipboard}')
b('P', 'open -t -- {clipboard}')
b('<ctrl-d>', 'scroll-page 0 0.2')
b('<ctrl-u>', 'scroll-page 0 -0.2')
b('<escape>', 'fake-key <escape>;;clear-messages;;jseval --quiet document.activeElement.blur();document.querySelector("body").click()')

config.unbind('<ctrl-w>')
config.unbind('<ctrl-n>')
config.unbind('<ctrl-p>')
b_all('<cmd-r>', 'reload')
b_all('<cmd-n>', 'open -w')
b('<ctrl-c>', 'fake-key -g <escape>', mode='command')

b('<ctrl-u>', 'fake-key <cmd-shift-left>;;fake-key <delete>', mode='insert')
b('<ctrl-k>', 'fake-key <cmd-shift-right>;;fake-key <delete>', mode='insert')
b('<ctrl-w>', 'fake-key <alt-backspace>', mode='insert')
b('<cmd-shift-left>', 'back')
b('ZQ', 'close')
b_all('<cmd-ctrl-l>', 'devtools-focus')
b_all('<cmd-ctrl-h>', 'devtools-focus')
b('<ctrl-w>', 'fake-key -g <alt-backspace>', mode='command')
b('<ctrl-j>', 'tab-give')
b('<ctrl-k>', 'set-cmd-text --space :tab-give')


## Developer settings
b('<space>d', 'devtools right')
