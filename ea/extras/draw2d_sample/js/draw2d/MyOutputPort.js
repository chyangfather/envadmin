draw2d.MyOutputPort=function(_393a){
draw2d.OutputPort.call(this,_393a);
};
draw2d.MyOutputPort.prototype=new draw2d.OutputPort();
draw2d.MyOutputPort.prototype.type="MyOutputPort";
draw2d.MyOutputPort.prototype.onDrop=function(port){
if(this.getMaxFanOut()<=this.getFanOut()){
return;
}
if(this.parentNode.id==port.parentNode.id){
}else{
var _393c=new draw2d.CommandConnect(this.parentNode.workflow,this,port);
_393c.setConnection(new draw2d.DecoratedConnection());
this.parentNode.workflow.getCommandStack().execute(_393c);
}
};
