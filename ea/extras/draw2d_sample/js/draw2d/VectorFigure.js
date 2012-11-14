/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

draw2d.VectorFigure=function(){this.bgColor=null;this.lineColor=new draw2d.Color(0,0,0);this.stroke=1;this.graphics=null;draw2d.Node.call(this);};draw2d.VectorFigure.prototype=new draw2d.Node;draw2d.VectorFigure.prototype.type="draw2d.VectorFigure";draw2d.VectorFigure.prototype.dispose=function(){draw2d.Node.prototype.dispose.call(this);this.bgColor=null;this.lineColor=null;if(this.graphics!=null){this.graphics.clear();}this.graphics=null;};draw2d.VectorFigure.prototype.createHTMLElement=function(){var item=draw2d.Node.prototype.createHTMLElement.call(this);item.style.border="0px";item.style.backgroundColor="transparent";return item;};draw2d.VectorFigure.prototype.setWorkflow=function(_2eb0){draw2d.Node.prototype.setWorkflow.call(this,_2eb0);if(this.workflow==null){this.graphics.clear();this.graphics=null;}};draw2d.VectorFigure.prototype.paint=function(){if(this.graphics==null){this.graphics=new jsGraphics(this.id);}else{this.graphics.clear();}draw2d.Node.prototype.paint.call(this);for(var i=0;i<this.ports.getSize();i++){this.getHTMLElement().appendChild(this.ports.get(i).getHTMLElement());}};draw2d.VectorFigure.prototype.setDimension=function(w,h){draw2d.Node.prototype.setDimension.call(this,w,h);if(this.graphics!=null){this.paint();}};draw2d.VectorFigure.prototype.setBackgroundColor=function(color){this.bgColor=color;if(this.graphics!=null){this.paint();}};draw2d.VectorFigure.prototype.getBackgroundColor=function(){return this.bgColor;};draw2d.VectorFigure.prototype.setLineWidth=function(w){this.stroke=w;if(this.graphics!=null){this.paint();}};draw2d.VectorFigure.prototype.setColor=function(color){this.lineColor=color;if(this.graphics!=null){this.paint();}};draw2d.VectorFigure.prototype.getColor=function(){return this.lineColor;};