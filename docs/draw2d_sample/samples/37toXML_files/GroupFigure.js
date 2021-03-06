draw2d.GroupFigure=function(title){
if(title){
this.title=title;
}else{
this.title="";
}
this.titlebar=null;
this.defaultBackgroundColor=new draw2d.Color(230,230,250);
this.highlightBackgroundColor=new draw2d.Color(250,250,200);
draw2d.CompartmentFigure.call(this);
this.setBackgroundColor(this.defaultBackgroundColor);
};
draw2d.GroupFigure.prototype=new draw2d.CompartmentFigure();
draw2d.GroupFigure.prototype.type="GroupFigure";
draw2d.GroupFigure.prototype.createHTMLElement=function(){
var item=draw2d.CompartmentFigure.prototype.createHTMLElement.call(this);
item.style.margin="0px";
item.style.padding="0px";
item.style.border="1px solid black";
item.style.cursor=null;
this.titlebar=document.createElement("div");
this.titlebar.style.position="absolute";
this.titlebar.style.left="0px";
this.titlebar.style.top="0px";
this.titlebar.style.width=(this.getWidth()-5)+"px";
this.titlebar.style.height="15px";
this.titlebar.style.margin="0px";
this.titlebar.style.padding="0px";
this.titlebar.style.font="normal 10px verdana";
this.titlebar.style.backgroundColor="blue";
this.titlebar.style.borderBottom="1px solid gray";
this.titlebar.style.borderLeft="5px solid transparent";
this.titlebar.style.whiteSpace="nowrap";
this.titlebar.style.textAlign="left";
this.titlebar.style.backgroundImage="url(window_toolbar.png)";
this.textNode=document.createTextNode(this.title);
this.titlebar.appendChild(this.textNode);
item.appendChild(this.titlebar);
return item;
};
draw2d.GroupFigure.prototype.onFigureEnter=function(_2de5){
if(this.children[_2de5.id]===null){
this.setBackgroundColor(this.highlightBackgroundColor);
}
draw2d.CompartmentFigure.prototype.onFigureEnter.call(this,_2de5);
};
draw2d.GroupFigure.prototype.onFigureLeave=function(_2de6){
draw2d.CompartmentFigure.prototype.onFigureLeave.call(this,_2de6);
this.setBackgroundColor(this.defaultBackgroundColor);
};
draw2d.GroupFigure.prototype.onFigureDrop=function(_2de7){
draw2d.CompartmentFigure.prototype.onFigureDrop.call(this,_2de7);
this.setBackgroundColor(this.defaultBackgroundColor);
};
draw2d.GroupFigure.prototype.setDimension=function(w,h){
draw2d.CompartmentFigure.prototype.setDimension.call(this,w,h);
if(this.titlebar!==null){
this.titlebar.style.width=(this.getWidth()-5)+"px";
}
};
draw2d.GroupFigure.prototype.setTitle=function(title){
this.title=title;
};
draw2d.GroupFigure.prototype.getMinWidth=function(){
return 50;
};
draw2d.GroupFigure.prototype.getMinHeight=function(){
return 50;
};
draw2d.GroupFigure.prototype.setBackgroundColor=function(color){
this.bgColor=color;
if(this.bgColor!==null){
this.html.style.backgroundColor=this.bgColor.getHTMLStyle();
}else{
this.html.style.backgroundColor="transparent";
}
};
