//jquery 插件对象
 
/**
 *
 * 序列话一个表单,并给该表单中每一个字段添加别名
 * @author jt.tao QQ:1453566283
 * @param {Object} n 表单对象别名
 * @memberOf {TypeName}
 * @return {TypeName}
 */
$.fn.serializeObjectForm = function(n)
{

    //if(!n) { alert('序列化表单请给别名!'); return null};//在此临时简单处理n，还有待你们完善呀...
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name]) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            if(this.value != ""){
                o[this.name].push( this.value );
            }
        } else {
            if(this.value != ""){
                o[this.name] = this.value;
            }
        }
    });
    return o;
};