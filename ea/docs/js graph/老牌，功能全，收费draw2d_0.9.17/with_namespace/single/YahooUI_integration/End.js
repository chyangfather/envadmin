draw2d.End=function(){
	draw2d.ImageFigure.call(this,"End.png");
	this.inputPort=null;
	this.setDimension(50,50);};
	draw2d.End.prototype=new draw2d.ImageFigure;
	draw2d.End.prototype.type="draw2d.End";
	draw2d.End.prototype.setWorkflow=function(_4d6d){
		draw2d.ImageFigure.prototype.setWorkflow.call(this,_4d6d);
		if(_4d6d!=null&&this.inputPort==null){
			this.inputPort=new draw2d.MyInputPort();
			this.inputPort.setWorkflow(_4d6d);
			this.inputPort.setBackgroundColor(new draw2d.Color(115,115,245));
			this.inputPort.setColor(null);
			this.addPort(this.inputPort,0,this.height/2);
			this.inputPort2=new draw2d.MyOutputPort();
			this.inputPort2.setWorkflow(_4d6d);
			this.inputPort2.setBackgroundColor(new draw2d.Color(245,115,115));
			this.inputPort2.setColor(null);this.addPort(this.inputPort2,this.width/2,0);
			this.inputPort3=new draw2d.MyOutputPort();
			this.inputPort3.setWorkflow(_4d6d);
			this.inputPort3.setBackgroundColor(new draw2d.Color(245,115,115));
			this.inputPort3.setColor(null);
			this.addPort(this.inputPort3,this.width,this.height/2);
			this.inputPort4=new draw2d.MyOutputPort();
			this.inputPort4.setWorkflow(_4d6d);
			this.inputPort4.setBackgroundColor(new draw2d.Color(245,115,115));
			this.inputPort4.setColor(null);
			this.addPort(this.inputPort4,this.width/2,this.height);
			}};