        function initTable() {
        $('#tb_workers').bootstrapTable('destroy');
        $('#tb_workers').bootstrapTable({
        url: "/online/index/get_sbbx/", //请求后台的URL（*）
        method: 'get', //请求方式（*）
        toolbar: '#toolbar',
        striped: true, //是否显示行间隔色
        cache: false, //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true, //是否显示分页（*）,
        sidePagination: 'client',
        sortable: true, //是否启用排序
        sortName: 'repair_no',
        sortOrder: 'desc', //排序方式
        sortStable: true,
        queryParamsType: "limit",//传递参数（*）
        pageNumber: 1, //初始化加载第一页，默认第一页
        pageSize: 100, //每页的记录行数（*）
        pageList: [10, 25, 50, 100], //可供选择的每页的行数（*）
        strictSearch: false,
        showColumns: true, //是否显示所有的列
        showRefresh: true, //是否显示刷新按钮
        minimumCountColumns: 2, //最少允许的列数
        uniqueId: "repair_no", //每一行的唯一标识，一般为主键列
        showToggle: true, //是否显示详细视图和列表视图的切换按钮
        cardView: false, //是否显示详细视图
        detailView: false, //是否显示父子表
        clickToSelect: true,
        search: true,
        singleSelect: true,
        columns: [{
                checkbox:true
                },{
                    field: 'repair_no',
                    title: '报修编号',
                    },{
                    field: 'de_no',
                    title: '设备编号',
                    },{
                    field: 'st_no',
                    title: '员工编号',
                    },{
                    field: 'destroy_date',
                    title: '损坏时间',
                    editable: {
                        type: 'text',
                        title: '损坏时间',
                        validate: function (v) {
                            if (!v) return '损坏时间不能为空';
                            }
                        }
                    },{
                    field: 'repair_num',
                    title: '损坏数量',
                    },{
                    field: 'beizhu',
                    title: '备注',
                    editable: {
                        type: 'text',
                        title: '备注',
                    }
                }],
                onEditableSave: function (field, row, oldValue, $el) {
                $.ajax({
                    type: "post",
                    url: "/online/index/edit_sbbx/",
                    data: row,
                    dataType: 'JSON',
                    success: function (ret) {
                        var last=JSON.stringify(ret);
                        if (last[10] == "1")
                        {
                            alert("编辑成功！");
                            $('#tb_workers').bootstrapTable("refresh");
                        }
                        else{
                            alert('编辑失败!');
                            $('#tb_workers').bootstrapTable("refresh");
                        }
                    },
                    error: function () {
                        alert('编辑失败!');
                        $('#tb_workers').bootstrapTable("refresh");
                    },
                    complete: function () {

                    }

                });
            }
        });

        }

          $(document).ready(function () {
              //调用函数，初始化表格
              initTable();
              //alert("666");
              //当点击查询按钮的时候执行
//              $("#btn_delete").click(function(){
//                alert("666");
//                var a=tb_workers.bootstrapTable('getSelections');
//                if (a.length==1)
//                {
//                    alert("yesyesyes");
//                }else {
//                    alert("nonono");
//                }
//                $.post("/online/index/delete_user/",{'way':1},
//                function(ret){$('#result').html(ret.result)},
//              }
          });


        function add_user()
        {
//            alert("66666");
//            var ss=document.getElementById("ygbh").value;
////            alert(ss);
//            var yy=null;
//            var cho=document.getElementById("basic_validate").st_sex;
////            alert(cho.length);
//            for (var i=0;i<cho.length;i++){
//                if (cho[i].checked){
//                    yy=cho[i].value;
//                }
//            }
//            alert(yy);

            $.post("/online/index/add_sbbx/",{

                'repair_no' : "0",
                'de_no' : document.getElementById("sbbh").value,
                'st_no' : document.getElementById("ygbh").value,
                'destroy_date' : document.getElementById("shsj").value,
                'repair_num' : document.getElementById("shsl").value,
                'beizhu' : document.getElementById("bz").value,
            },
            function(ret){
                var last=JSON.stringify(ret);
                if (last[10] == "1")
                {
                    alert("添加成功！");
                    $('#tb_workers').bootstrapTable("refresh");
                }
                else{
                    alert("添加失败");
                    $('#tb_workers').bootstrapTable("refresh");
                }
            }
            )
        }


        function showmymtk()
        {
            $('#myModal').modal();
        }