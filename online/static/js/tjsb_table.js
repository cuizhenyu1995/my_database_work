        function initTable() {
        $('#tb_workers').bootstrapTable('destroy');
        $('#tb_workers').bootstrapTable({
        url: "/online/index/get_device/", //请求后台的URL（*）
        method: 'get', //请求方式（*）
        toolbar: '#toolbar',
        striped: true, //是否显示行间隔色
        cache: false, //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
        pagination: true, //是否显示分页（*）,
        sidePagination: 'client',
        sortable: true, //是否启用排序
        sortName: 'de_no',
        sortOrder: 'asc', //排序方式
        sortStable: true,
        queryParamsType: "limit",//传递参数（*）
        pageNumber: 1, //初始化加载第一页，默认第一页
        pageSize: 100, //每页的记录行数（*）
        pageList: [10, 25, 50, 100], //可供选择的每页的行数（*）
        strictSearch: false,
        showColumns: true, //是否显示所有的列
        showRefresh: true, //是否显示刷新按钮
        minimumCountColumns: 2, //最少允许的列数
        uniqueId: "de_no", //每一行的唯一标识，一般为主键列
        showToggle: true, //是否显示详细视图和列表视图的切换按钮
        cardView: false, //是否显示详细视图
        detailView: false, //是否显示父子表
        clickToSelect: true,
        search: true,
        singleSelect: true,
        columns: [{
                checkbox:true
                },{
                    field: 'de_no',
                    title: '设备编号',
                    },{
                    field: 'de_name',
                    title: '设备名称',
                    editable: {
                        type: 'text',
                        title: '设备名称',
                        validate: function (v) {
                            if (!v) return '设备名称不能为空';
                            }
                        }
                    },{
                    field: 'de_allnum',
                    title: '设备总个数',
                    },{
                    field: 'de_repnum',
                    title: '设备维修数',
                    },{
                    field: 'de_lennum',
                    title: '设备借出数',
                    },{
                    field: 'de_lasnum',
                    title: '可用设备数',
                }],
                onEditableSave: function (field, row, oldValue, $el) {
                $.ajax({
                    type: "post",
                    url: "/online/index/edit_device/",
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

        function del_user()
        {
            var rows=$("#tb_workers").bootstrapTable('getSelections',function(row)
            {
                return row;
            });
//            alert("23333");
            $.post("/online/index/delete_device/",{
                'del_no' : rows[0].de_no,
            },
            function(ret){
                var last=JSON.stringify(ret);
                if (last[10] == "1")
                {
                    alert("删除成功！");
                    $('#tb_workers').bootstrapTable("refresh");
                }
                else{
                    alert("删除失败");
                    $('#tb_workers').bootstrapTable("refresh");
                }
            }
            )
        }

        function add_user()
        {
            $.post("/online/index/add_device/",{

                'de_no' : document.getElementById("ygbh").value,
                'de_name' : document.getElementById("ygxm").value,
                'de_allnum' : "0",
                'de_repnum' : "0",
                'de_lennum' : "0",
                'de_lasnum' : "0",
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