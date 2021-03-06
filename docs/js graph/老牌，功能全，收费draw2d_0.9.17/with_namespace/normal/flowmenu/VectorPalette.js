/* This notice must be untouched at all times.

Open-jACOB Draw2D
The latest version is available at
http://www.openjacob.org

Copyright (c) 2006 Andreas Herz. All rights reserved.
Created 5. 11. 2006 by Andreas Herz (Web: http://www.freegroup.de )

LICENSE: LGPL

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License (LGPL) as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA,
or see http://www.gnu.org/copyleft/lesser.html
*/

draw2d.VectorPalette=function()
{
  draw2d.ToolPalette.call(this, "Tools");

  // undo / redo support
  //
  this.undoTool = new draw2d.ToolUndo(this);
  this.undoTool.setPosition(13,10);
  this.undoTool.setEnabled(false);
  this.addChild(this.undoTool);


  this.redoTool = new draw2d.ToolRedo(this);
  this.redoTool.setPosition(43,10);
  this.redoTool.setEnabled(false);
  this.addChild(this.redoTool);

  this.setDimension(170,53);
}

draw2d.VectorPalette.prototype = new draw2d.ToolPalette;
/** @private */
draw2d.VectorPalette.prototype.type="VectorPalette";


draw2d.VectorPalette.prototype.onSetDocumentDirty=function()
{
  this.undoTool.setEnabled(this.workflow.getCommandStack().canUndo());
  this.redoTool.setEnabled(this.workflow.getCommandStack().canRedo());
}
