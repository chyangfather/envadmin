draw2d.MyOutputPort=
function(_60ee)
{draw2d.OutputPort.call(this,_60ee);};
draw2d.MyOutputPort.prototype=new draw2d.OutputPort;
draw2d.MyOutputPort.prototype.onDrop=function(port)
{if(this.getMaxFanOut()<=this.getFanOut())
{return;}
if(this.parentNode.id==port.parentNode.id)
{}
else
{var _60f0=new draw2d.CommandConnect(this.parentNode.workflow,this,port);
_60f0.setConnection(new draw2d.ArrowConnection());
this.parentNode.workflow.getCommandStack().execute(_60f0);}};