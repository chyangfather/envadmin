draw2d.SelectionHighlighter=function(_576b){this.workflow=_576b;this.counter=0;this.black=new draw2d.Color(0,0,0);this.gray=new draw2d.Color(200,200,200);};draw2d.SelectionHighlighter.prototype.type="SelectionHighlighter";draw2d.SelectionHighlighter.prototype.onSelectionChanged=function(_576c){this.counter++;debugLabel.setText("Count:"+this.counter);var alpha=(_576c==null)?1:0.2;var color=(_576c==null)?this.black:this.gray;var doc=this.workflow.getDocument();var _5770=doc.getFigures();for(var i=0;i<_5770.getSize();i++){_5770.get(i).setAlpha(alpha);}var lines=doc.getLines();for(var i=0;i<lines.getSize();i++){lines.get(i).setColor(color);}if(_576c!=null){_576c.setAlpha(1);if(_576c instanceof draw2d.Node){var ports=_576c.getPorts();for(var i=0;i<ports.getSize();i++){var port=ports.get(i);var _5775=port.getConnections();for(var j=0;j<_5775.getSize();j++){_5775.get(j).setColor(this.black);}}}}};