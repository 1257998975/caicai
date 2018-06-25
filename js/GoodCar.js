$(document).ready(function () {
    $('.tj').click(function () {

        $.ajax({
            url: "SalesMax",
            type: "POST",
            data: $('#form1').serialize(),
            // success: function (data) {
            //
            //     alert(data["data"].Goods_name);
            //
            //
            //     var localData = [
            //         {
            //             "count": 1,
            //             "title": data["data"].Goods_name,
            //             "time": "9月8日"
            //         },
            //         {
            //             "count": 2,
            //             "title": data["data"].Goods_name,
            //             "time": "9月8日"
            //         },
            //         {
            //             "count": 3,
            //             "title": "爱情",
            //             "time": "9月8日"
            //         },
            //         {
            //             "count": 4,
            //             "title": "外国文学",
            //             "time": "9月8日"
            //         }
            //     ]
            //
            // }
        });


// 定义数据出口
        module.exports = {
            postList: localData
        }
    });
});