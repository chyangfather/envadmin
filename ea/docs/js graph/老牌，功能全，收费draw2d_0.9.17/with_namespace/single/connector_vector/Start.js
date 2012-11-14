draw2d.Start=function()
{	
	draw2d.ImageFigure.call(this,this.type+".png");
	this.outputPort=null;
	this.setDimension(50,50);
};
draw2d.Start.prototype=new draw2d.ImageFigure;
draw2d.Start.prototype.type="Start";
draw2d.Start.prototype.setWorkflow=function(_51d8)
{
	draw2d.ImageFigure.prototype.setWorkflow.call(this,_51d8);
	if(_51d8!=null&&this.outputPort==null)
	{
		this.outputPort=new draw2d.MyOutputPort();
		this.outputPort.setMaxFanOut(5);
		this.outputPort.setWorkflow(_51d8);
		this.outputPort.setBackgroundColor(new draw2d.Color(245,115,115));
		this.addPort(this.outputPort,this.width,this.height/2);
	}
};