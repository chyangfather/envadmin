LS74xx=function(title){
this.title=title;
Node.call(this);
this.out1=null;
this.out2=null;
this.out3=null;
this.out4=null;
this.out5=null;
this.out6=null;
this.out7=null;
this.out8=null;
this.in1=null;
this.in2=null;
this.in3=null;
this.in4=null;
this.in5=null;
this.in6=null;
this.in7=null;
this.in8=null;
this.setColor(new Color(255,128,255));
this.setBackgroundColor(new Color(245,245,255));
this.setDimension(250,50);
};
LS74xx.prototype=new Node;
LS74xx.prototype.type="LS74xx";
LS74xx.prototype.createHTMLElement=function(){
var item=CompartmentFigure.prototype.createHTMLElement.call(this);
this.label=document.createElement("div");
this.label.style.position="absolute";
this.label.style.left="0px";
this.label.style.top="5px";
this.label.style.width="100%";
this.label.style.height=(this.getHeight()-10)+"px";
this.label.style.font="normal 10px verdana";
this.label.style.textAlign="center";
this.textNode=document.createTextNode(this.title);
this.label.appendChild(this.textNode);
item.appendChild(this.label);
this.slot=document.createElement("img");
this.slot.src="slot.png";
this.slot.style.position="absolute";
this.slot.style.left="0px";
this.slot.style.top=(this.getHeight()/2-7)+"px";
item.appendChild(this.slot);
return item;
};
LS74xx.prototype.setWorkflow=function(_35c0){
Node.prototype.setWorkflow.call(this,_35c0);
if(_35c0!=null&&this.out1==null){
var _35c1=this.width/8;
var dHalf=_35c1/2;
this.out1=new OutputPort();
this.out1.setWorkflow(_35c0);
this.addPort(this.out1,_35c1*1-dHalf,this.height);
this.out2=new OutputPort();
this.out2.setWorkflow(_35c0);
this.addPort(this.out2,_35c1*2-dHalf,this.height);
this.out3=new OutputPort();
this.out3.setWorkflow(_35c0);
this.addPort(this.out3,_35c1*3-dHalf,this.height);
this.out4=new OutputPort();
this.out4.setWorkflow(_35c0);
this.addPort(this.out4,_35c1*4-dHalf,this.height);
this.out5=new OutputPort();
this.out5.setWorkflow(_35c0);
this.addPort(this.out5,_35c1*5-dHalf,this.height);
this.out6=new OutputPort();
this.out6.setWorkflow(_35c0);
this.addPort(this.out6,_35c1*6-dHalf,this.height);
this.out7=new OutputPort();
this.out7.setWorkflow(_35c0);
this.addPort(this.out7,_35c1*7-dHalf,this.height);
this.out8=new OutputPort();
this.out8.setWorkflow(_35c0);
this.addPort(this.out8,_35c1*8-dHalf,this.height);
this.in1=new InputPort();
this.in1.setWorkflow(_35c0);
this.in1.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in1,_35c1*1-dHalf,0);
this.in2=new InputPort();
this.in2.setWorkflow(_35c0);
this.in2.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in2,_35c1*2-dHalf,0);
this.in3=new InputPort();
this.in3.setWorkflow(_35c0);
this.in3.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in3,_35c1*3-dHalf,0);
this.in4=new InputPort();
this.in4.setWorkflow(_35c0);
this.in4.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in4,_35c1*4-dHalf,0);
this.in5=new InputPort();
this.in5.setWorkflow(_35c0);
this.in5.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in5,_35c1*5-dHalf,0);
this.in6=new InputPort();
this.in6.setWorkflow(_35c0);
this.in6.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in6,_35c1*6-dHalf,0);
this.in7=new InputPort();
this.in7.setWorkflow(_35c0);
this.in7.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in7,_35c1*7-dHalf,0);
this.in8=new InputPort();
this.in8.setWorkflow(_35c0);
this.in8.setBackgroundColor(new Color(255,128,128));
this.addPort(this.in8,_35c1*8-dHalf,0);
}
};
LS74xx.prototype.setDimension=function(w,h){
Node.prototype.setDimension.call(this,w,h);
if(this.label!=null){
this.label.style.height=(this.getHeight()-10)+"px";
this.slot.style.top=((this.getHeight()/2)-7)+"px";
}
if(this.out1!=null){
var _35c5=this.width/8;
var dHalf=_35c5/2;
this.out1.setPosition(_35c5*1-dHalf,this.height);
this.out2.setPosition(_35c5*2-dHalf,this.height);
this.out3.setPosition(_35c5*3-dHalf,this.height);
this.out4.setPosition(_35c5*4-dHalf,this.height);
this.out5.setPosition(_35c5*5-dHalf,this.height);
this.out6.setPosition(_35c5*6-dHalf,this.height);
this.out7.setPosition(_35c5*7-dHalf,this.height);
this.out8.setPosition(_35c5*8-dHalf,this.height);
this.in1.setPosition(_35c5*1-dHalf,0);
this.in2.setPosition(_35c5*2-dHalf,0);
this.in3.setPosition(_35c5*3-dHalf,0);
this.in4.setPosition(_35c5*4-dHalf,0);
this.in5.setPosition(_35c5*5-dHalf,0);
this.in6.setPosition(_35c5*6-dHalf,0);
this.in7.setPosition(_35c5*7-dHalf,0);
this.in8.setPosition(_35c5*8-dHalf,0);
}
};
LS74xx.prototype.onMouseEnter=function(){
this.setColor(new Color(255,0,255));
};
LS74xx.prototype.onMouseLeave=function(){
this.setColor(new Color(255,128,255));
};
