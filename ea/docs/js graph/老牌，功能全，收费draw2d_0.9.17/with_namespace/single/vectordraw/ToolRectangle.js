draw2d.ToolRectangle=function(_5a70){draw2d.ToolGeneric.call(this,_5a70);};draw2d.ToolRectangle.prototype=new draw2d.ToolGeneric;draw2d.ToolRectangle.prototype.type="ToolRectangle";draw2d.ToolRectangle.prototype.execute=function(x,y){var _5a73=new draw2d.Rectangle();_5a73.setDimension(100,60);_5a73.setBackgroundColor(new draw2d.Color(255,255,255));this.palette.workflow.getCommandStack().execute(new draw2d.CommandAdd(this.palette.workflow,_5a73,x,y));draw2d.ToolGeneric.prototype.execute.call(this,x,y);};