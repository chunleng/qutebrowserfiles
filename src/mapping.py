def setup(config):
    def bind_in_all_mode(key, command):
        for mode in ("normal", "insert", "hint", "passthrough", "command", "prompt", "yesno", "caret", "register"):
            config.bind(key, command, mode=mode)

    bind_in_all_mode("<Ctrl-Meta-P>", ":tab-prev")
    bind_in_all_mode("<Ctrl-Meta-N>", ":tab-next")
    config.bind("o", ":cmd-set-text :open {url};;fake-key -g <Meta-left><Alt-right><Meta-shift-right>")
    config.bind("t", ":cmd-set-text :open -t {url};;fake-key -g <Meta-left><Alt-right><right><right><right><Meta-shift-right>")
    config.bind("<Meta-t>", ":open -t")
    config.bind("w", ":cmd-set-text :open -w {url};;fake-key -g <Meta-left><Alt-right><right><right><right><Meta-shift-right>")
    config.bind("W", ":cmd-set-text :open -p {url};;fake-key -g <Meta-left><Alt-right><right><right><right><Meta-shift-right>")
    config.bind("<Meta-n>", ":open -w")
    config.bind("<Meta-shift-n>", ":open -p")

    config.bind("<Ctrl-j>", ":tab-give")
    config.bind("<Ctrl-k>", ":cmd-set-text --space :tab-give")

    bind_in_all_mode("<Meta-r>", ":reload")
    bind_in_all_mode("<Meta-w>", ":tab-close -o")
    config.bind("<Ctrl-q>", ":tab-close -o")
    config.unbind("<Ctrl-w>")
    config.bind("<Ctrl-w>q", ":close")

    config.bind("<Ctrl-p>", ":tab-prev")
    config.bind("<Ctrl-n>", ":tab-next")
    config.bind("<space>bo", ":tab-only -P keep")
    config.bind("<space>bh", ":tab-only -P keep -n")
    config.bind("<space>bl", ":tab-only -P keep -p")
    config.bind("<space>ba", ":open -t;;tab-only -P keep;;tab-close")
    config.bind("gp", ":tab-pin")
    config.bind("g1", ":tab-focus 1")
    config.bind("g2", ":tab-focus 2")
    config.bind("g3", ":tab-focus 3")
    config.bind("g4", ":tab-focus 4")
    config.bind("g5", ":tab-focus 5")
    config.bind("g6", ":tab-focus 6")
    config.bind("g7", ":tab-focus 7")
    config.bind("g8", ":tab-focus 8")
    config.bind("g9", ":tab-focus 9")
    config.bind("<backspace>", ":tab-focus last")

    config.bind("0", "zoom")

    bind_in_all_mode("<Ctrl-Meta-,>", ":tab-move -")
    bind_in_all_mode("<Ctrl-Meta-.>", ":tab-move +")
    config.bind("<Ctrl-,>", ":tab-move -")
    config.bind("<Ctrl-.>", ":tab-move +")

    config.bind("p", ":open -- {clipboard}")
    config.bind("P", ":open -t -- {clipboard}")

    config.bind("<Ctrl-o>", ":back")
    config.bind("<Meta-left>", ":back")
    config.bind("<Ctrl-i>", ":forward")
    config.bind("<Meta-right>", ":forward")

    config.bind("<space>tt", ":jseval -q -f ~/.qutebrowser/js/translate.js")
    config.bind("<space>gq", ":spawn -u qr.sh {url}")
    config.bind("<space>d", ":devtools")
    config.bind("<Ctrl-space>a", ":spawn -u lpass.py", mode="insert")
    config.bind("<Ctrl-space>u", ":spawn -u lpass.py --username-only", mode="insert")
    config.bind("<Ctrl-space>p", ":spawn -u lpass.py --password-only", mode="insert")

    config.bind("<Ctrl-u>", ":fake-key <Ctrl-backspace>", mode="insert")
    config.bind("<Ctrl-w>", ":fake-key <Alt-Shift-left>;;fake-key <backspace>", mode="insert")
    config.bind("<Ctrl-k>", ":fake-key <Meta-Shift-right>;;fake-key <backspace>", mode="insert")
    config.unbind("<Ctrl-a>")
    config.bind("<Ctrl-a>", ":fake-key <Meta-left>", mode="insert")
    config.bind("<Ctrl-e>", ":fake-key <Meta-right>", mode="insert")

    config.unbind("b")
    config.bind("b", ":cmd-set-text --space :bookmark-load")

    config.bind("<Esc>", ":search;;fake-key <Esc>")
    config.bind("<Esc>", ":mode-enter normal;;jseval -q document.activeElement.blur()", mode="insert")
    bind_in_all_mode("<Ctrl-c>", "mode-enter normal")
    config.bind("m", ":bookmark-add")

    bind_in_all_mode("<Meta-q>", ":quit --save")

    config.bind("<Ctrl-d>", ":cmd-repeat 12 scroll down")
    config.bind("<Ctrl-u>", ":cmd-repeat 12 scroll up")

    config.unbind("d")
    config.unbind("D")
    config.bind("D", ":download")
    config.bind("dd", ":download")

    config.bind("F", ":hint links tab-fg")
    config.bind("gf", ":hint -r links tab-bg")
    config.bind("yf", ":hint links yank")
    config.bind("df", ":hint all download")

    config.bind("[", ":navigate prev")
    config.bind("]", ":navigate next")

    config.bind("<Meta-a>", ":fake-key -g <Meta-left><Meta-Shift-right>", mode="command")
    config.bind("<Return>", ":cmd-set-text --space :tab-select", mode="normal")
    config.bind("<Ctrl-i>", ":edit-text", mode="insert")
