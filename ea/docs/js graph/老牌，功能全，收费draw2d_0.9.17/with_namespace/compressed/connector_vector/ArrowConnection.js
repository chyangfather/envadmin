/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

draw2d.ArrowConnection=function(){draw2d.ArrowLine.call(this);this.sourcePort=null;this.targetPort=null;this.lineSegments=new Array();this.setColor(new draw2d.Color(0,0,115));this.setLineWidth(1);};draw2d.ArrowConnection.prototype=new draw2d.ArrowLine;draw2d.ArrowConnection.prototype.type="ArrowConnection";draw2d.ArrowConnection.prototype.disconnect=function(){if(this.sourcePort!=null){this.sourcePort.detachMoveListener(this);}if(this.targetPort!=null){this.targetPort.detachMoveListener(this);}};draw2d.ArrowConnection.prototype.reconnect=function(){if(this.sourcePort!=null){this.sourcePort.attachMoveListener(this);}if(this.targetPort!=null){this.targetPort.attachMoveListener(this);}};draw2d.ArrowConnection.prototype.isConnector=function(){return true;};draw2d.ArrowConnection.prototype.isResizeable=function(){return false;};draw2d.ArrowConnection.prototype.setSource=function(port){if(this.sourcePort!=null){this.sourcePort.detachMoveListener(this);}this.sourcePort=port;if(this.sourcePort==null){return;}this.sourcePort.attachMoveListener(this);this.setStartPoint(port.getAbsoluteX(),port.getAbsoluteY());};draw2d.ArrowConnection.prototype.getSource=function(){return this.sourcePort;};draw2d.ArrowConnection.prototype.setTarget=function(port){if(this.targetPort!=null){this.targetPort.detachMoveListener(this);}this.targetPort=port;if(this.targetPort==null){return;}this.targetPort.attachMoveListener(this);this.setEndPoint(port.getAbsoluteX(),port.getAbsoluteY());};draw2d.ArrowConnection.prototype.getTarget=function(){return this.targetPort;};draw2d.ArrowConnection.prototype.onOtherFigureMoved=function(_1853){if(_1853==this.sourcePort){this.setStartPoint(this.sourcePort.getAbsoluteX(),this.sourcePort.getAbsoluteY());}else{this.setEndPoint(this.targetPort.getAbsoluteX(),this.targetPort.getAbsoluteY());}};