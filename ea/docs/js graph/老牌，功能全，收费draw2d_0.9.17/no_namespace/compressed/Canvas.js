/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

Canvas=function(_1257){if(_1257){this.construct(_1257);}this.enableSmoothFigureHandling=false;this.canvasLines=new ArrayList();};Canvas.prototype.type="Canvas";Canvas.prototype.construct=function(_1258){this.canvasId=_1258;this.html=document.getElementById(this.canvasId);this.scrollArea=document.body.parentNode;};Canvas.prototype.setViewPort=function(divId){this.scrollArea=document.getElementById(divId);};Canvas.prototype.addFigure=function(_125a,xPos,yPos,_125d){if(this.enableSmoothFigureHandling==true){if(_125a.timer<=0){_125a.setAlpha(0.001);}var _125e=_125a;var _125f=function(){if(_125e.alpha<1){_125e.setAlpha(Math.min(1,_125e.alpha+0.05));}else{window.clearInterval(_125e.timer);_125e.timer=-1;}};if(_125e.timer>0){window.clearInterval(_125e.timer);}_125e.timer=window.setInterval(_125f,30);}_125a.setCanvas(this);if(xPos&&yPos){_125a.setPosition(xPos,yPos);}if(_125a instanceof Line){this.canvasLines.add(_125a);this.html.appendChild(_125a.getHTMLElement());}else{var obj=this.canvasLines.getFirstElement();if(obj==null){this.html.appendChild(_125a.getHTMLElement());}else{this.html.insertBefore(_125a.getHTMLElement(),obj.getHTMLElement());}}if(!_125d){_125a.paint();}};Canvas.prototype.removeFigure=function(_1261){if(this.enableSmoothFigureHandling==true){var oThis=this;var _1263=_1261;var _1264=function(){if(_1263.alpha>0){_1263.setAlpha(Math.max(0,_1263.alpha-0.05));}else{window.clearInterval(_1263.timer);_1263.timer=-1;oThis.html.removeChild(_1263.html);_1263.setCanvas(null);}};if(_1263.timer>0){window.clearInterval(_1263.timer);}_1263.timer=window.setInterval(_1264,20);}else{this.html.removeChild(_1261.html);_1261.setCanvas(null);}if(_1261 instanceof Line){this.canvasLines.remove(_1261);}};Canvas.prototype.getEnableSmoothFigureHandling=function(){return this.enableSmoothFigureHandling;};Canvas.prototype.setEnableSmoothFigureHandling=function(flag){this.enableSmoothFigureHandling=flag;};Canvas.prototype.getWidth=function(){return parseInt(this.html.style.width);};Canvas.prototype.getHeight=function(){return parseInt(this.html.style.height);};Canvas.prototype.setBackgroundImage=function(_1266,_1267){if(_1266!=null){if(_1267){this.html.style.background="transparent url("+_1266+") ";}else{this.html.style.background="transparent url("+_1266+") no-repeat";}}else{this.html.style.background="transparent";}};Canvas.prototype.getY=function(){return this.y;};Canvas.prototype.getX=function(){return this.x;};Canvas.prototype.getAbsoluteY=function(){var el=this.html;var ot=el.offsetTop;while((el=el.offsetParent)!=null){ot+=el.offsetTop;}return ot;};Canvas.prototype.getAbsoluteX=function(){var el=this.html;var ol=el.offsetLeft;while((el=el.offsetParent)!=null){ol+=el.offsetLeft;}return ol;};Canvas.prototype.getScrollLeft=function(){return this.scrollArea.scrollLeft;};Canvas.prototype.getScrollTop=function(){return this.scrollArea.scrollTop;};