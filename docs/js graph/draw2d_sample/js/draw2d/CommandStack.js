/**
This notice must be untouched at all times.
This is the COMPRESSED version of Draw2D
WebSite: http://www.draw2d.org
Copyright: 2006 Andreas Herz. All rights reserved.
Created: 5.11.2006 by Andreas Herz (Web: http://www.freegroup.de )
LICENSE: LGPL
**/

draw2d.CommandStack=function(){this.undostack=new Array();this.redostack=new Array();this.maxundo=50;this.eventListeners=new draw2d.ArrayList();};draw2d.CommandStack.PRE_EXECUTE=1;draw2d.CommandStack.PRE_REDO=2;draw2d.CommandStack.PRE_UNDO=4;draw2d.CommandStack.POST_EXECUTE=8;draw2d.CommandStack.POST_REDO=16;draw2d.CommandStack.POST_UNDO=32;draw2d.CommandStack.POST_MASK=draw2d.CommandStack.POST_EXECUTE|draw2d.CommandStack.POST_UNDO|draw2d.CommandStack.POST_REDO;draw2d.CommandStack.PRE_MASK=draw2d.CommandStack.PRE_EXECUTE|draw2d.CommandStack.PRE_UNDO|draw2d.CommandStack.PRE_REDO;draw2d.CommandStack.prototype.type="draw2d.CommandStack";draw2d.CommandStack.prototype.setUndoLimit=function(count){this.maxundo=count;};draw2d.CommandStack.prototype.markSaveLocation=function(){this.undostack=new Array();this.redostack=new Array();};draw2d.CommandStack.prototype.execute=function(_1e7b){if(_1e7b==null){return;}if(_1e7b.canExecute()==false){return;}this.notifyListeners(_1e7b,draw2d.CommandStack.PRE_EXECUTE);this.undostack.push(_1e7b);_1e7b.execute();this.redostack=new Array();if(this.undostack.length>this.maxundo){this.undostack=this.undostack.slice(this.undostack.length-this.maxundo);}this.notifyListeners(_1e7b,draw2d.CommandStack.POST_EXECUTE);};draw2d.CommandStack.prototype.undo=function(){var _1e7c=this.undostack.pop();if(_1e7c){this.notifyListeners(_1e7c,draw2d.CommandStack.PRE_UNDO);this.redostack.push(_1e7c);_1e7c.undo();this.notifyListeners(_1e7c,draw2d.CommandStack.POST_UNDO);}};draw2d.CommandStack.prototype.redo=function(){var _1e7d=this.redostack.pop();if(_1e7d){this.notifyListeners(_1e7d,draw2d.CommandStack.PRE_REDO);this.undostack.push(_1e7d);_1e7d.redo();this.notifyListeners(_1e7d,draw2d.CommandStack.POST_REDO);}};draw2d.CommandStack.prototype.canRedo=function(){return this.redostack.length>0;};draw2d.CommandStack.prototype.canUndo=function(){return this.undostack.length>0;};draw2d.CommandStack.prototype.addCommandStackEventListener=function(_1e7e){this.eventListeners.add(_1e7e);};draw2d.CommandStack.prototype.removeCommandStackEventListener=function(_1e7f){this.eventListeners.remove(_1e7f);};draw2d.CommandStack.prototype.notifyListeners=function(_1e80,state){var event=new draw2d.CommandStackEvent(_1e80,state);var size=this.eventListeners.getSize();for(var i=0;i<size;i++){this.eventListeners.get(i).stackChanged(event);}};