(() => {
    var host = document.location.host;
    if (!host) {
        return ;
    }

    if (host.endsWith(".translate.goog")) {
        host = document.location.host.replace(/.translate.goog$/, "").replaceAll("-",".").replaceAll("..", "-");
        document.location = `https://${host}${document.location.pathname}`;
    } else {
        host = document.location.host.replaceAll("-","--").replaceAll(".","-");
        document.location = `https://${host}.translate.goog${document.location.pathname}?_x_tr_sl=auto&_x_tr_tl=en`
    }
})()

