jQuery.fn._height=jQuery.fn.height;
jQuery.fn._width=jQuery.fn.width;
jQuery.fn.height=function(){
if(this[0]==window){
return self.innerHeight||jQuery.boxModel&&document.documentElement.clientHeight||document.body.clientHeight;
}
if(this[0]==document){
return Math.max(document.body.scrollHeight,document.body.offsetHeight);
}
return this._height(arguments[0]);
};
jQuery.fn.width=function(){
if(this[0]==window){
return self.innerWidth||jQuery.boxModel&&document.documentElement.clientWidth||document.body.clientWidth;
}
if(this[0]==document){
return Math.max(document.body.scrollWidth,document.body.offsetWidth);
}
return this._width(arguments[0]);
};
jQuery.fn.innerHeight=function(){
return this[0]==window||this[0]==document?this.height():this.css("display")!="none"?this[0].offsetHeight-(parseInt(this.css("borderTopWidth"))||0)-(parseInt(this.css("borderBottomWidth"))||0):this.height()+(parseInt(this.css("paddingTop"))||0)+(parseInt(this.css("paddingBottom"))||0);
};
jQuery.fn.innerWidth=function(){
return this[0]==window||this[0]==document?this.width():this.css("display")!="none"?this[0].offsetWidth-(parseInt(this.css("borderLeftWidth"))||0)-(parseInt(this.css("borderRightWidth"))||0):this.height()+(parseInt(this.css("paddingLeft"))||0)+(parseInt(this.css("paddingRight"))||0);
};
jQuery.fn.outerHeight=function(){
return this[0]==window||this[0]==document?this.height():this.css("display")!="none"?this[0].offsetHeight:this.height()+(parseInt(this.css("borderTopWidth"))||0)+(parseInt(this.css("borderBottomWidth"))||0)+(parseInt(this.css("paddingTop"))||0)+(parseInt(this.css("paddingBottom"))||0);
};
jQuery.fn.outerWidth=function(){
return this[0]==window||this[0]==document?this.width():this.css("display")!="none"?this[0].offsetWidth:this.height()+(parseInt(this.css("borderLeftWidth"))||0)+(parseInt(this.css("borderRightWidth"))||0)+(parseInt(this.css("paddingLeft"))||0)+(parseInt(this.css("paddingRight"))||0);
};
jQuery.fn.scrollLeft=function(){
if(this[0]==window||this[0]==document){
return self.pageXOffset||jQuery.boxModel&&document.documentElement.scrollLeft||document.body.scrollLeft;
}
return this[0].scrollLeft;
};
jQuery.fn.scrollTop=function(){
if(this[0]==window||this[0]==document){
return self.pageYOffset||jQuery.boxModel&&document.documentElement.scrollTop||document.body.scrollTop;
}
return this[0].scrollTop;
};
jQuery.fn.offset=function(_3916,_3917){
var x=0,y=0,elem=this[0],parent=this[0],sl=0,st=0,_3916=jQuery.extend({margin:true,border:true,padding:false,scroll:true},_3916||{});
do{
x+=parent.offsetLeft||0;
y+=parent.offsetTop||0;
if(jQuery.browser.mozilla||jQuery.browser.msie){
var bt=parseInt(jQuery.css(parent,"borderTopWidth"))||0;
var bl=parseInt(jQuery.css(parent,"borderLeftWidth"))||0;
x+=bl;
y+=bt;
if(jQuery.browser.mozilla&&parent!=elem&&jQuery.css(parent,"overflow")!="visible"){
x+=bl;
y+=bt;
}
}
var op=parent.offsetParent;
if(op&&(op.tagName=="BODY"||op.tagName=="HTML")){
if(jQuery.browser.safari&&jQuery.css(parent,"position")!="absolute"){
x+=parseInt(jQuery.css(op,"marginLeft"))||0;
y+=parseInt(jQuery.css(op,"marginTop"))||0;
}
break;
}
if(_3916.scroll){
do{
sl+=parent.scrollLeft||0;
st+=parent.scrollTop||0;
parent=parent.parentNode;
if(jQuery.browser.mozilla&&parent!=elem&&parent!=op&&parent.style&&jQuery.css(parent,"overflow")!="visible"){
y+=parseInt(jQuery.css(parent,"borderTopWidth"))||0;
x+=parseInt(jQuery.css(parent,"borderLeftWidth"))||0;
}
}while(parent!=op);
}else{
parent=parent.offsetParent;
}
}while(parent);
if(!_3916.margin){
x-=parseInt(jQuery.css(elem,"marginLeft"))||0;
y-=parseInt(jQuery.css(elem,"marginTop"))||0;
}
if(_3916.border&&(jQuery.browser.safari||jQuery.browser.opera)){
x+=parseInt(jQuery.css(elem,"borderLeftWidth"))||0;
y+=parseInt(jQuery.css(elem,"borderTopWidth"))||0;
}else{
if(!_3916.border&&!(jQuery.browser.safari||jQuery.browser.opera)){
x-=parseInt(jQuery.css(elem,"borderLeftWidth"))||0;
y-=parseInt(jQuery.css(elem,"borderTopWidth"))||0;
}
}
if(_3916.padding){
x+=parseInt(jQuery.css(elem,"paddingLeft"))||0;
y+=parseInt(jQuery.css(elem,"paddingTop"))||0;
}
if(_3916.scroll&&jQuery.browser.opera&&jQuery.css(elem,"display")=="inline"){
sl-=elem.scrollLeft||0;
st-=elem.scrollTop||0;
}
var _391c=_3916.scroll?{top:y-st,left:x-sl,scrollTop:st,scrollLeft:sl}:{top:y,left:x};
if(_3917){
jQuery.extend(_3917,_391c);
return this;
}else{
return _391c;
}
};
jQuery.fn.ajaxSubmit=function(_391d){
if(typeof _391d=="function"){
_391d={success:_391d};
}
_391d=jQuery.extend({url:this.attr("action")||"",method:this.attr("method")||"GET"},_391d||{});
_391d.success=_391d.success||_391d.after;
_391d.beforeSubmit=_391d.beforeSubmit||_391d.before;
_391d.type=_391d.type||_391d.method;
var a=this.formToArray(_391d.semantic);
if(_391d.beforeSubmit&&_391d.beforeSubmit(a,this,_391d)===false){
return this;
}
var q=jQuery.param(a);
if(_391d.type.toUpperCase()=="GET"){
_391d.url+=(_391d.url.indexOf("?")>=0?"&":"?")+q;
_391d.data=null;
}else{
_391d.data=q;
}
var $form=this,callbacks=[];
if(_391d.resetForm){
callbacks.push(function(){
$form.resetForm();
});
}
if(_391d.clearForm){
callbacks.push(function(){
$form.clearForm();
});
}
if(!_391d.dataType&&_391d.target){
var _3921=_391d.success||function(){
};
callbacks.push(function(data,_3923){
jQuery(_391d.target).attr("innerHTML",data).evalScripts().each(_3921,[data,_3923]);
});
}else{
if(_391d.success){
callbacks.push(_391d.success);
}
}
_391d.success=function(data,_3925){
for(var i=0,max=callbacks.length;i<max;i++){
callbacks[i](data,_3925);
}
};
jQuery.ajax(_391d);
return this;
};
jQuery.fn.ajaxForm=function(_3927){
return this.each(function(){
jQuery("input:submit,input:image,button:submit",this).click(function(ev){
var $form=this.form;
$form.clk=this;
if(this.type=="image"){
if(ev.offsetX!=undefined){
$form.clk_x=ev.offsetX;
$form.clk_y=ev.offsetY;
}else{
if(typeof jQuery.fn.offset=="function"){
var _392a=jQuery(this).offset();
$form.clk_x=ev.pageX-_392a.left;
$form.clk_y=ev.pageY-_392a.top;
}else{
$form.clk_x=ev.pageX-this.offsetLeft;
$form.clk_y=ev.pageY-this.offsetTop;
}
}
}
setTimeout(function(){
$form.clk=$form.clk_x=$form.clk_y=null;
},10);
});
}).submit(function(e){
jQuery(this).ajaxSubmit(_3927);
return false;
});
};
jQuery.fn.formToArray=function(_392c){
var a=[];
if(this.length==0){
return a;
}
var form=this[0];
var els=_392c?form.getElementsByTagName("*"):form.elements;
if(!els){
return a;
}
for(var i=0,max=els.length;i<max;i++){
var el=els[i];
var n=el.name;
if(!n){
continue;
}
if(_392c&&form.clk&&el.type=="image"){
if(!el.disabled&&form.clk==el){
a.push({name:n+".x",value:form.clk_x},{name:n+".y",value:form.clk_y});
}
continue;
}
var v=jQuery.fieldValue(el,true);
if(v===null){
continue;
}
if(v.constructor==Array){
for(var j=0,jmax=v.length;j<jmax;j++){
a.push({name:n,value:v[j]});
}
}else{
a.push({name:n,value:v});
}
}
if(!_392c&&form.clk){
var _3935=form.getElementsByTagName("input");
for(var i=0,max=_3935.length;i<max;i++){
var input=_3935[i];
var n=input.name;
if(n&&!input.disabled&&input.type=="image"&&form.clk==input){
a.push({name:n+".x",value:form.clk_x},{name:n+".y",value:form.clk_y});
}
}
}
return a;
};
jQuery.fn.formSerialize=function(_3937){
return jQuery.param(this.formToArray(_3937));
};
jQuery.fn.fieldSerialize=function(_3938){
var a=[];
this.each(function(){
var n=this.name;
if(!n){
return;
}
var v=jQuery.fieldValue(this,_3938);
if(v&&v.constructor==Array){
for(var i=0,max=v.length;i<max;i++){
a.push({name:n,value:v[i]});
}
}else{
if(v!==null&&typeof v!="undefined"){
a.push({name:this.name,value:v});
}
}
});
return jQuery.param(a);
};
jQuery.fn.fieldValue=function(_393d){
var cbVal,cbName;
for(var i=0,max=this.length;i<max;i++){
var el=this[i];
var v=jQuery.fieldValue(el,_393d);
if(v===null||typeof v=="undefined"||(v.constructor==Array&&!v.length)){
continue;
}
if(el.type!="checkbox"){
return v;
}
cbName=cbName||el.name;
if(cbName!=el.name){
return cbVal;
}
cbVal=cbVal||[];
cbVal.push(v);
}
return cbVal;
};
jQuery.fieldValue=function(el,_3943){
var n=el.name,t=el.type,tag=el.tagName.toLowerCase();
if(typeof _3943=="undefined"){
_3943=true;
}
if(_3943&&(!n||el.disabled||t=="reset"||(t=="checkbox"||t=="radio")&&!el.checked||(t=="submit"||t=="image")&&el.form&&el.form.clk!=el||tag=="select"&&el.selectedIndex==-1)){
return null;
}
if(tag=="select"){
var index=el.selectedIndex;
if(index<0){
return null;
}
var a=[],ops=el.options;
var one=(t=="select-one");
var max=(one?index+1:ops.length);
for(var i=(one?index:0);i<max;i++){
var op=ops[i];
if(op.selected){
var v=jQuery.browser.msie&&!(op.attributes["value"].specified)?op.text:op.value;
if(one){
return v;
}
a.push(v);
}
}
return a;
}
return el.value;
};
jQuery.fn.clearForm=function(){
return this.each(function(){
jQuery("input,select,textarea",this).clearFields();
});
};
jQuery.fn.clearFields=jQuery.fn.clearInputs=function(){
return this.each(function(){
var t=this.type,tag=this.tagName.toLowerCase();
if(t=="text"||t=="password"||tag=="textarea"){
this.value="";
}else{
if(t=="checkbox"||t=="radio"){
this.checked=false;
}else{
if(tag=="select"){
this.selectedIndex=-1;
}
}
}
});
};
jQuery.fn.resetForm=function(){
return this.each(function(){
if(typeof this.reset=="function"||(typeof this.reset=="object"&&!this.reset.nodeType)){
this.reset();
}
});
};
