draw2d.MyGraphicalEditorFactory=function(){draw2d.EditPartFactory.call(this);};draw2d.MyGraphicalEditorFactory.prototype=new draw2d.EditPartFactory;draw2d.MyGraphicalEditorFactory.prototype.type="draw2d.MyGraphicalEditorFactory";draw2d.MyGraphicalEditorFactory.prototype.createEditPart=function(model){var _4db6;if(model instanceof draw2d.TableModel){_4db6=new draw2d.TableFigure();}if(model instanceof draw2d.ForeignKeyModel){_4db6=new draw2d.ForeignKeyFigure();}if(_4db6==null){alert("factory called with unknown model class:"+model.type);}_4db6.setModel(model);return _4db6;};