/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

draw2d.Port=function(_211b,_211c){Corona=function(){};Corona.prototype=new draw2d.Circle;Corona.prototype.setAlpha=function(_211d){draw2d.Circle.prototype.setAlpha.call(this,Math.min(0.3,_211d));};if(_211b==null){this.currentUIRepresentation=new draw2d.Circle();}else{this.currentUIRepresentation=_211b;}if(_211c==null){this.connectedUIRepresentation=new draw2d.Circle();this.connectedUIRepresentation.setColor(null);}else{this.connectedUIRepresentation=_211c;}this.disconnectedUIRepresentation=this.currentUIRepresentation;this.hideIfConnected=false;this.uiRepresentationAdded=true;this.parentNode=null;this.originX=0;this.originY=0;this.coronaWidth=10;this.corona=null;draw2d.Rectangle.call(this);this.setDimension(8,8);this.setBackgroundColor(new draw2d.Color(100,180,100));this.setColor(new draw2d.Color(90,150,90));draw2d.Rectangle.prototype.setColor.call(this,null);this.dropable=new draw2d.DropTarget(this.html);this.dropable.node=this;this.dropable.addEventListener("dragenter",function(_211e){_211e.target.node.onDragEnter(_211e.relatedTarget.node);});this.dropable.addEventListener("dragleave",function(_211f){_211f.target.node.onDragLeave(_211f.relatedTarget.node);});this.dropable.addEventListener("drop",function(_2120){_2120.relatedTarget.node.onDrop(_2120.target.node);});};draw2d.Port.prototype=new draw2d.Rectangle;draw2d.Port.prototype.type="draw2d.Port";draw2d.Port.ZOrderBaseIndex=5000;draw2d.Port.setZOrderBaseIndex=function(index){draw2d.Port.ZOrderBaseIndex=index;};draw2d.Port.prototype.setHideIfConnected=function(flag){this.hideIfConnected=flag;};draw2d.Port.prototype.dispose=function(){var size=this.moveListener.getSize();for(var i=0;i<size;i++){var _2125=this.moveListener.get(i);this.parentNode.workflow.removeFigure(_2125);_2125.dispose();}draw2d.Rectangle.prototype.dispose.call(this);this.parentNode=null;this.dropable.node=null;this.dropable=null;this.disconnectedUIRepresentation.dispose();this.connectedUIRepresentation.dispose();};draw2d.Port.prototype.createHTMLElement=function(){var item=draw2d.Rectangle.prototype.createHTMLElement.call(this);item.style.zIndex=draw2d.Port.ZOrderBaseIndex;this.currentUIRepresentation.html.zIndex=draw2d.Port.ZOrderBaseIndex;item.appendChild(this.currentUIRepresentation.html);this.uiRepresentationAdded=true;return item;};draw2d.Port.prototype.setUiRepresentation=function(_2127){if(_2127==null){_2127=new draw2d.Figure();}if(this.uiRepresentationAdded){this.html.removeChild(this.currentUIRepresentation.getHTMLElement());}this.html.appendChild(_2127.getHTMLElement());_2127.paint();this.currentUIRepresentation=_2127;};draw2d.Port.prototype.onMouseEnter=function(){this.setLineWidth(2);};draw2d.Port.prototype.onMouseLeave=function(){this.setLineWidth(0);};draw2d.Port.prototype.setDimension=function(width,_2129){draw2d.Rectangle.prototype.setDimension.call(this,width,_2129);this.connectedUIRepresentation.setDimension(width,_2129);this.disconnectedUIRepresentation.setDimension(width,_2129);this.setPosition(this.x,this.y);};draw2d.Port.prototype.setBackgroundColor=function(color){this.currentUIRepresentation.setBackgroundColor(color);};draw2d.Port.prototype.getBackgroundColor=function(){return this.currentUIRepresentation.getBackgroundColor();};draw2d.Port.prototype.getConnections=function(){var _212b=new draw2d.ArrayList();var size=this.moveListener.getSize();for(var i=0;i<size;i++){var _212e=this.moveListener.get(i);if(_212e instanceof draw2d.Connection){_212b.add(_212e);}}return _212b;};draw2d.Port.prototype.setColor=function(color){this.currentUIRepresentation.setColor(color);};draw2d.Port.prototype.getColor=function(){return this.currentUIRepresentation.getColor();};draw2d.Port.prototype.setLineWidth=function(width){this.currentUIRepresentation.setLineWidth(width);};draw2d.Port.prototype.getLineWidth=function(){return this.currentUIRepresentation.getLineWidth();};draw2d.Port.prototype.paint=function(){this.currentUIRepresentation.paint();};draw2d.Port.prototype.setPosition=function(xPos,yPos){this.originX=xPos;this.originY=yPos;draw2d.Rectangle.prototype.setPosition.call(this,xPos,yPos);if(this.html==null){return;}this.html.style.left=(this.x-this.getWidth()/2)+"px";this.html.style.top=(this.y-this.getHeight()/2)+"px";};draw2d.Port.prototype.setParent=function(_2133){if(this.parentNode!=null){this.parentNode.detachMoveListener(this);}this.parentNode=_2133;if(this.parentNode!=null){this.parentNode.attachMoveListener(this);}};draw2d.Port.prototype.attachMoveListener=function(_2134){draw2d.Rectangle.prototype.attachMoveListener.call(this,_2134);if(this.hideIfConnected==true){this.setUiRepresentation(this.connectedUIRepresentation);}};draw2d.Port.prototype.detachMoveListener=function(_2135){draw2d.Rectangle.prototype.detachMoveListener.call(this,_2135);if(this.getConnections().getSize()==0){this.setUiRepresentation(this.disconnectedUIRepresentation);}};draw2d.Port.prototype.getParent=function(){return this.parentNode;};draw2d.Port.prototype.onDrag=function(){draw2d.Rectangle.prototype.onDrag.call(this);this.parentNode.workflow.showConnectionLine(this.parentNode.x+this.x,this.parentNode.y+this.y,this.parentNode.x+this.originX,this.parentNode.y+this.originY);};draw2d.Port.prototype.getCoronaWidth=function(){return this.coronaWidth;};draw2d.Port.prototype.setCoronaWidth=function(width){this.coronaWidth=width;};draw2d.Port.prototype.setOrigin=function(x,y){this.originX=x;this.originY=y;};draw2d.Port.prototype.onDragend=function(){this.setAlpha(1);this.setPosition(this.originX,this.originY);this.parentNode.workflow.hideConnectionLine();};draw2d.Port.prototype.onDragEnter=function(port){this.parentNode.workflow.connectionLine.setColor(new draw2d.Color(0,150,0));this.parentNode.workflow.connectionLine.setLineWidth(3);this.showCorona(true);};draw2d.Port.prototype.onDragLeave=function(port){this.parentNode.workflow.connectionLine.setColor(new draw2d.Color(0,0,0));this.parentNode.workflow.connectionLine.setLineWidth(1);this.showCorona(false);};draw2d.Port.prototype.onDrop=function(port){var _213c=new draw2d.EditPolicy(draw2d.EditPolicy.CONNECT);_213c.canvas=this.parentNode.workflow;_213c.source=port;_213c.target=this;var _213d=this.createCommand(_213c);if(_213d!=null){this.parentNode.workflow.getCommandStack().execute(_213d);}};draw2d.Port.prototype.getAbsolutePosition=function(){return new draw2d.Point(this.getAbsoluteX(),this.getAbsoluteY());};draw2d.Port.prototype.getAbsoluteBounds=function(){return new draw2d.Dimension(this.getAbsoluteX(),this.getAbsoluteY(),this.getWidth(),this.getHeight());};draw2d.Port.prototype.getAbsoluteY=function(){return this.originY+this.parentNode.getY();};draw2d.Port.prototype.getAbsoluteX=function(){return this.originX+this.parentNode.getX();};draw2d.Port.prototype.onOtherFigureMoved=function(_213e){this.fireMoveEvent();};draw2d.Port.prototype.getName=function(){return this.name;};draw2d.Port.prototype.setName=function(name){this.name=name;};draw2d.Port.prototype.isOver=function(iX,iY){var x=this.getAbsoluteX()-this.coronaWidth-this.getWidth()/2;var y=this.getAbsoluteY()-this.coronaWidth-this.getHeight()/2;var iX2=x+this.width+(this.coronaWidth*2)+this.getWidth()/2;var iY2=y+this.height+(this.coronaWidth*2)+this.getHeight()/2;return (iX>=x&&iX<=iX2&&iY>=y&&iY<=iY2);};draw2d.Port.prototype.showCorona=function(flag,_2147){if(flag==true){this.corona=new Corona();this.corona.setAlpha(0.3);this.corona.setBackgroundColor(new draw2d.Color(0,125,125));this.corona.setColor(null);this.corona.setDimension(this.getWidth()+(this.getCoronaWidth()*2),this.getWidth()+(this.getCoronaWidth()*2));this.parentNode.getWorkflow().addFigure(this.corona,this.getAbsoluteX()-this.getCoronaWidth()-this.getWidth()/2,this.getAbsoluteY()-this.getCoronaWidth()-this.getHeight()/2);}else{if(flag==false&&this.corona!=null){this.parentNode.getWorkflow().removeFigure(this.corona);this.corona=null;}}};draw2d.Port.prototype.createCommand=function(_2148){if(_2148.getPolicy()==draw2d.EditPolicy.MOVE){return new draw2d.CommandMovePort(this);}if(_2148.getPolicy()==draw2d.EditPolicy.CONNECT){if(_2148.source.parentNode.id==_2148.target.parentNode.id){return null;}else{return new draw2d.CommandConnect(_2148.canvas,_2148.source,_2148.target);}}return null;};