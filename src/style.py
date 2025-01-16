def setup(c):
    black = "#1d1f21"
    white = "#e0e0e0"
    gray = "#373b41"
    gray_2 = "#666a70"
    green = "#323d2f"
    blue = "#456887"
    red = "#cc6666"
    yellow = "#b5bd68"
    purple = "#793270"
    black_rgba = "rgba(29,31,33,0.9)"
    gray_rgba = "rgba(55,59,65,0.5)"
    white = "rgba(224,224,224,0.9)"

    c.window.hide_decoration = True
    c.fonts.default_family = "Arial"
    c.fonts.default_size = "14pt"
    c.fonts.statusbar = "13pt Menlo"
    c.fonts.completion.category = "bold 13pt Menlo"
    c.fonts.completion.entry = "13pt Menlo"

    c.colors.tabs.bar.bg = black
    c.colors.tabs.odd.bg = black
    c.colors.tabs.odd.fg = white
    c.colors.tabs.even.bg = black
    c.colors.tabs.even.fg = white
    c.colors.tabs.pinned.odd.bg = green
    c.colors.tabs.pinned.even.fg = white
    c.colors.tabs.pinned.even.bg = green
    c.colors.tabs.pinned.even.fg = white
    c.colors.tabs.pinned.selected.odd.bg = blue
    c.colors.tabs.pinned.selected.odd.fg = white
    c.colors.tabs.pinned.selected.even.bg = blue
    c.colors.tabs.pinned.selected.even.fg = white
    c.colors.tabs.selected.odd.bg = blue
    c.colors.tabs.selected.odd.fg = white
    c.colors.tabs.selected.even.bg = blue
    c.colors.tabs.selected.even.fg = white

    c.colors.contextmenu.menu.bg = black
    c.colors.contextmenu.menu.fg = white
    c.colors.contextmenu.disabled.fg = gray
    c.colors.contextmenu.selected.bg = blue

    c.colors.completion.category.fg = white
    c.colors.completion.category.bg = gray_rgba
    c.colors.completion.category.border.top = "transparent"
    c.colors.completion.category.border.bottom = "transparent"
    c.colors.completion.fg = white
    c.colors.completion.odd.bg = black_rgba
    c.colors.completion.even.bg = black_rgba
    c.colors.completion.scrollbar.fg = white
    c.colors.completion.scrollbar.bg = black
    c.colors.completion.match.fg = blue
    c.colors.completion.item.selected.match.fg = white
    c.colors.completion.item.selected.bg = blue
    c.colors.completion.item.selected.fg = black
    c.colors.completion.item.selected.border.top = "transparent"
    c.colors.completion.item.selected.border.bottom = "transparent"

    c.colors.statusbar.normal.bg = black
    c.colors.statusbar.normal.fg = white
    c.colors.statusbar.command.private.bg = black
    c.colors.statusbar.command.private.fg = white
    c.colors.statusbar.private.bg = purple
    c.colors.statusbar.private.fg = white
    c.colors.statusbar.insert.bg = yellow
    c.colors.statusbar.insert.fg = black
    c.colors.statusbar.caret.bg = blue
    c.colors.statusbar.caret.fg = black
    c.colors.statusbar.caret.selection.bg = blue
    c.colors.statusbar.caret.selection.fg = black
    c.colors.statusbar.passthrough.bg = yellow
    c.colors.statusbar.passthrough.fg = black

    c.colors.statusbar.url.success.http.fg = red
    c.colors.statusbar.url.success.https.fg = gray_2
    c.colors.statusbar.url.warn.fg = yellow
    c.colors.statusbar.url.error.fg = red
    c.colors.statusbar.url.hover.fg = white

    c.colors.downloads.bar.bg = black
    c.colors.downloads.start.bg = white
    c.colors.downloads.start.fg = black
    c.colors.downloads.stop.bg = black
    c.colors.downloads.stop.fg = white
    c.colors.downloads.error.bg = red
    c.colors.downloads.error.fg = black

    c.colors.messages.error.fg = black
    c.colors.messages.error.bg = red
    c.colors.messages.error.border = "transparent"
    c.colors.messages.info.fg = black
    c.colors.messages.info.bg = blue
    c.colors.messages.info.border = "transparent"
    c.colors.messages.warning.fg = black
    c.colors.messages.warning.bg = yellow
    c.colors.messages.warning.border = "transparent"
