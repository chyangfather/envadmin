/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

ArrowConnection=function(){ArrowLine.call(this);this.sourcePort=null;this.targetPort=null;this.lineSegments=new Array();this.setColor(new Color(0,0,115));this.setLineWidth(1);};ArrowConnection.prototype=new ArrowLine;ArrowConnection.prototype.type="ArrowConnection";ArrowConnection.prototype.disconnect=function(){if(this.sourcePort!=null){this.sourcePort.detachMoveListener(this);}if(this.targetPort!=null){this.targetPort.detachMoveListener(this);}};ArrowConnection.prototype.reconnect=function(){if(this.sourcePort!=null){this.sourcePort.attachMoveListener(this);}if(this.targetPort!=null){this.targetPort.attachMoveListener(this);}};ArrowConnection.prototype.isConnector=function(){return true;};ArrowConnection.prototype.isResizeable=function(){return false;};ArrowConnection.prototype.setSource=function(port){if(this.sourcePort!=null){this.sourcePort.detachMoveListener(this);}this.sourcePort=port;if(this.sourcePort==null){return;}this.sourcePort.attachMoveListener(this);this.setStartPoint(port.getAbsoluteX(),port.getAbsoluteY());};ArrowConnection.prototype.getSource=function(){return this.sourcePort;};ArrowConnection.prototype.setTarget=function(port){if(this.targetPort!=null){this.targetPort.detachMoveListener(this);}this.targetPort=port;if(this.targetPort==null){return;}this.targetPort.attachMoveListener(this);this.setEndPoint(port.getAbsoluteX(),port.getAbsoluteY());};ArrowConnection.prototype.getTarget=function(){return this.targetPort;};ArrowConnection.prototype.onOtherFigureMoved=function(_1594){if(_1594==this.sourcePort){this.setStartPoint(this.sourcePort.getAbsoluteX(),this.sourcePort.getAbsoluteY());}else{this.setEndPoint(this.targetPort.getAbsoluteX(),this.targetPort.getAbsoluteY());}};