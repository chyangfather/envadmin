draw2d.shape.uml.InheritanceConnection=function(){
draw2d.Connection.call(this);
this.setTargetDecorator(new draw2d.shape.uml.InheritanceConnectionDecorator());
this.setSourceAnchor(new draw2d.ChopboxConnectionAnchor());
this.setTargetAnchor(new draw2d.ChopboxConnectionAnchor());
this.setRouter(new draw2d.NullConnectionRouter());
};
draw2d.shape.uml.InheritanceConnection.prototype=new draw2d.Connection();
