draw2d.MyInputPort=
function(_4b7b)
{draw2d.InputPort.call(this,_4b7b);};
draw2d.MyInputPort.prototype=new draw2d.InputPort;
draw2d.MyInputPort.prototype.onDrop=function(port)
{if(port.getMaxFanOut&&port.getMaxFanOut()<=port.getFanOut())
{return;}
if(this.parentNode.id==port.parentNode.id)
  {
  
  }
else
{var _4b7d=new draw2d.CommandConnect(this.parentNode.workflow,port,this);
    //CommandConnect()方法的函数体，三个参数，分别表示工作流，源和目的
   //draw2d.CommandConnect=function(_5176,_5177,_5178)
   //{draw2d.Command.call(this,"create connection");
   //this.workflow=_5176;this.source=_5177;this.target=_5178;
   //this.connection=null;};
_4b7d.setConnection(new draw2d.ArrowConnection());
this.parentNode.workflow.getCommandStack().execute(_4b7d);
}
};