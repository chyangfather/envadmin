/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

draw2d.Line=function(){this.lineColor=new draw2d.Color(0,0,0);this.stroke=1;this.canvas=null;this.workflow=null;this.html=null;this.graphics=null;this.id=draw2d.UUID.create();this.startX=30;this.startY=30;this.endX=100;this.endY=100;this.alpha=1;this.isMoving=false;this.model=null;this.zOrder=draw2d.Line.ZOrderBaseIndex;this.corona=draw2d.Line.CoronaWidth;this.properties=new Object();this.moveListener=new draw2d.ArrayList();this.setSelectable(true);this.setDeleteable(true);};draw2d.Line.prototype.type="draw2d.Line";draw2d.Line.ZOrderBaseIndex=200;draw2d.Line.ZOrderBaseIndex=200;draw2d.Line.CoronaWidth=5;draw2d.Line.setZOrderBaseIndex=function(index){draw2d.Line.ZOrderBaseIndex=index;};draw2d.Line.setDefaultCoronaWidth=function(width){draw2d.Line.CoronaWidth=width;};draw2d.Line.prototype.dispose=function(){this.canvas=null;this.workflow=null;if(this.graphics!=null){this.graphics.clear();}this.graphics=null;};draw2d.Line.prototype.getZOrder=function(){return this.zOrder;};draw2d.Line.prototype.setZOrder=function(index){if(this.html!=null){this.html.style.zIndex=index;}this.zOrder=index;};draw2d.Line.prototype.setCoronaWidth=function(width){this.corona=width;};draw2d.Line.prototype.createHTMLElement=function(){var item=document.createElement("div");item.id=this.id;item.style.position="absolute";item.style.left="0px";item.style.top="0px";item.style.height="0px";item.style.width="0px";item.style.zIndex=this.zOrder;return item;};draw2d.Line.prototype.setId=function(id){this.id=id;if(this.html!=null){this.html.id=id;}};draw2d.Line.prototype.getProperties=function(){return this.properties;};draw2d.Line.prototype.getProperty=function(key){return this.properties[key];};draw2d.Line.prototype.setProperty=function(key,value){this.properties[key]=value;this.setDocumentDirty();};draw2d.Line.prototype.getHTMLElement=function(){if(this.html==null){this.html=this.createHTMLElement();}return this.html;};draw2d.Line.prototype.getWorkflow=function(){return this.workflow;};draw2d.Line.prototype.isResizeable=function(){return true;};draw2d.Line.prototype.setCanvas=function(_1cc5){this.canvas=_1cc5;if(this.graphics!=null){this.graphics.clear();}this.graphics=null;};draw2d.Line.prototype.setWorkflow=function(_1cc6){this.workflow=_1cc6;if(this.graphics!=null){this.graphics.clear();}this.graphics=null;};draw2d.Line.prototype.paint=function(){if(this.graphics==null){this.graphics=new jsGraphics(this.id);}else{this.graphics.clear();}this.graphics.setStroke(this.stroke);this.graphics.setColor(this.lineColor.getHTMLStyle());this.graphics.drawLine(this.startX,this.startY,this.endX,this.endY);this.graphics.paint();};draw2d.Line.prototype.attachMoveListener=function(_1cc7){this.moveListener.add(_1cc7);};draw2d.Line.prototype.detachMoveListener=function(_1cc8){this.moveListener.remove(_1cc8);};draw2d.Line.prototype.fireMoveEvent=function(){var size=this.moveListener.getSize();for(var i=0;i<size;i++){this.moveListener.get(i).onOtherFigureMoved(this);}};draw2d.Line.prototype.onOtherFigureMoved=function(_1ccb){};draw2d.Line.prototype.setLineWidth=function(w){this.stroke=w;if(this.graphics!=null){this.paint();}this.setDocumentDirty();};draw2d.Line.prototype.setColor=function(color){this.lineColor=color;if(this.graphics!=null){this.paint();}this.setDocumentDirty();};draw2d.Line.prototype.getColor=function(){return this.lineColor;};draw2d.Line.prototype.setAlpha=function(_1cce){if(_1cce==this.alpha){return;}try{this.html.style.MozOpacity=_1cce;}catch(exc){}try{this.html.style.opacity=_1cce;}catch(exc){}try{var _1ccf=Math.round(_1cce*100);if(_1ccf>=99){this.html.style.filter="";}else{this.html.style.filter="alpha(opacity="+_1ccf+")";}}catch(exc){}this.alpha=_1cce;};draw2d.Line.prototype.setStartPoint=function(x,y){this.startX=x;this.startY=y;if(this.graphics!=null){this.paint();}this.setDocumentDirty();};draw2d.Line.prototype.setEndPoint=function(x,y){this.endX=x;this.endY=y;if(this.graphics!=null){this.paint();}this.setDocumentDirty();};draw2d.Line.prototype.getStartX=function(){return this.startX;};draw2d.Line.prototype.getStartY=function(){return this.startY;};draw2d.Line.prototype.getStartPoint=function(){return new draw2d.Point(this.startX,this.startY);};draw2d.Line.prototype.getEndX=function(){return this.endX;};draw2d.Line.prototype.getEndY=function(){return this.endY;};draw2d.Line.prototype.getEndPoint=function(){return new draw2d.Point(this.endX,this.endY);};draw2d.Line.prototype.isSelectable=function(){return this.selectable;};draw2d.Line.prototype.setSelectable=function(flag){this.selectable=flag;};draw2d.Line.prototype.isDeleteable=function(){return this.deleteable;};draw2d.Line.prototype.setDeleteable=function(flag){this.deleteable=flag;};draw2d.Line.prototype.getLength=function(){return Math.sqrt((this.startX-this.endX)*(this.startX-this.endX)+(this.startY-this.endY)*(this.startY-this.endY));};draw2d.Line.prototype.getAngle=function(){var _1cd6=this.getLength();var angle=-(180/Math.PI)*Math.asin((this.startY-this.endY)/_1cd6);if(angle<0){if(this.endX<this.startX){angle=Math.abs(angle)+180;}else{angle=360-Math.abs(angle);}}else{if(this.endX<this.startX){angle=180-angle;}}return angle;};draw2d.Line.prototype.createCommand=function(_1cd8){if(_1cd8.getPolicy()==draw2d.EditPolicy.MOVE){var x1=this.getStartX();var y1=this.getStartY();var x2=this.getEndX();var y2=this.getEndY();return new draw2d.CommandMoveLine(this,x1,y1,x2,y2);}if(_1cd8.getPolicy()==draw2d.EditPolicy.DELETE){if(this.isDeleteable()==false){return null;}return new draw2d.CommandDelete(this);}return null;};draw2d.Line.prototype.setModel=function(model){if(this.model!=null){this.model.removePropertyChangeListener(this);}this.model=model;if(this.model!=null){this.model.addPropertyChangeListener(this);}};draw2d.Line.prototype.getModel=function(){return this.model;};draw2d.Line.prototype.onContextMenu=function(x,y){var menu=this.getContextMenu();if(menu!=null){this.workflow.showMenu(menu,x,y);}};draw2d.Line.prototype.getContextMenu=function(){return null;};draw2d.Line.prototype.onDoubleClick=function(){};draw2d.Line.prototype.setDocumentDirty=function(){if(this.workflow!=null){this.workflow.setDocumentDirty();}};draw2d.Line.prototype.containsPoint=function(px,py){return draw2d.Line.hit(this.corona,this.startX,this.startY,this.endX,this.endY,px,py);};draw2d.Line.hit=function(_1ce3,X1,Y1,X2,Y2,px,py){X2-=X1;Y2-=Y1;px-=X1;py-=Y1;var _1cea=px*X2+py*Y2;var _1ceb;if(_1cea<=0){_1ceb=0;}else{px=X2-px;py=Y2-py;_1cea=px*X2+py*Y2;if(_1cea<=0){_1ceb=0;}else{_1ceb=_1cea*_1cea/(X2*X2+Y2*Y2);}}var lenSq=px*px+py*py-_1ceb;if(lenSq<0){lenSq=0;}return Math.sqrt(lenSq)<_1ce3;};