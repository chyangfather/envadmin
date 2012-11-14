draw2d.ArrowLine=function()
{this.lineColor=new draw2d.Color(0,0,0);
this.stroke=1;
this.canvas=null;
this.workflow=null;
this.html=null;
this.graphics=null;
this.id=draw2d.UUID.create();
this.startX=30;
this.startY=30;
this.endX=100;
this.endY=100;
this.zOrder=draw2d.ArrowLine.ZOrderBaseIndex;
this.setSelectable(true);
this.setDeleteable(true);
this.arrowWidth=10;
this.arrowLength=20;
this.lineWidth=5;};
draw2d.ArrowLine.prototype=new draw2d.Line;
draw2d.ArrowLine.prototype.type="draw2d.ArrowLine";
draw2d.ArrowLine.prototype.paint=function()
{         //重写paint方法，以重绘图像
if(this.graphics==null)  //如果图像为空，则新建一个图像
{
this.graphics=new jsGraphics(this.id);
}
else   //若不为空，先清空
{
this.graphics.clear();
}
this.graphics.setStroke(this.stroke);
this.graphics.setColor(this.lineColor.getHTMLStyle());
var endY=this.getLength();
var _4ea5=[0,0,endY-this.arrowLength,endY-this.arrowLength,endY,endY-this.arrowLength,endY-this.arrowLength,0];
var _4ea6=[-this.lineWidth,+this.lineWidth,+this.lineWidth,this.lineWidth+this.arrowWidth/2,0,-(this.lineWidth+this.arrowWidth/2),-this.lineWidth,-this.lineWidth];
var _4ea7=this.getAngle()*Math.PI/180;
var rotX=new Array();
var rotY=new Array();
for(var i=0;i<_4ea5.length;i++)
{
rotX[i]=this.startX+_4ea5[i]*Math.cos(_4ea7)-_4ea6[i]*Math.sin(_4ea7);
rotY[i]=this.startY+_4ea5[i]*Math.sin(_4ea7)+_4ea6[i]*Math.cos(_4ea7);}
this.graphics.drawPolyLine(rotX,rotY);
this.graphics.paint();
};