$(function(){
    // 表单验证
    $("#frmLogin").submit(function(){
        var uname = $("[name=uname]").val();
        var upwd = $("[name=upwd]").val();

        if(uname.length==0 || upwd.length==0){
            return false;
        }
        return true;
    });
});