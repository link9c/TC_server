let ad = $('.ad');
let ae = $('.ae');

$('.forward').click(function () {
    let code = $('._forward').children().eq(0).val();
    ae.css("display", "none");
    ad.css("display", "block");
    $.ajax({
        url: "/forward",
        type: "POST",
        data: {code: code},
        success: function (reply) {
            if (reply.code === 1002 || reply.code === 1003 ) {
                ad.css("display", "none");
                $('._forward a').attr('href', reply.path)
                ae.html("正向查找加载完成，请点击下载！")
                ae.css("display", "block");

            } else if (reply.code === 1001 || reply.code === 1000) {
                ad.css("display", "none");
                ae.html("正向查找未找到信息！")
                ae.css("display", "block");
            }
        }
    })
});

$('.backward').click(function () {
    let code = $('._backward').children().eq(0).val();
    ae.css("display", "none");
    ad.css("display", "block");
    $.ajax({
        url: "/backward",
        type: "POST",
        data: {code: code},
        success: function (reply) {
            if (reply.code === 1002 || reply.code === 1003) {
                ad.css("display", "none");
                $('._backward a').attr('href', reply.path);
                ae.html("反向查找加载完成，请点击下载！");
                ae.css("display", "block");
            } else if (reply.code === 1001 || reply.code === 1000) {
                ad.css("display", "none");
                ae.html("反向查找未找到信息！");
                ae.css("display", "block");
            }

        }
    })
})