alert("hello")
function ttt_loader() {
  var my_canvas = document.getElementById("myCanvas");
  var w = window.innerWidth;
  var h = window.innerHeight;
  var size = Math.min(w*0.66, h*0.66);
  my_canvas.width = size;
  my_canvas.height = size;
  my_canvas.style = "border:1px solid #000000; position:fixed; right: ".concat(((w-size)/2).toString()).concat("; bottom: ").concat(((h-size)/2).toString()).concat(";");
  var ctx = my_canvas.getContext("2d");
  draw_line(ctx,size/3,size/20,size/3,size-size/20);
  draw_line(ctx,2*size/3,size/20,2*size/3,size-size/20);
  draw_line(ctx,size/20,size/3,size-size/20,size/3);
  draw_line(ctx,size/20,2*size/3,size-size/20,2*size/3);
  
  // Add event listener for `click` events.
  my_canvas.addEventListener('click', function(event) {
    var x = event.pageX - (w-size)/2,
        y = event.pageY - (h-size)/2;
    var move = [Math.floor(y/(size/3)),Math.floor(x/(size/3))];
    draw_letter(ctx, "X", move[1], move[0]);
}, false);
}

function draw_line(ctx, s_x,s_y,e_x,e_y) {
  ctx.beginPath();
  ctx.lineWidth = 3;
  ctx.lineCap = "round";
  ctx.moveTo(s_x,s_y);
  ctx.lineTo(e_x, e_y);
  ctx.stroke();
}

function draw_letter(ctx, letter, x, y) {
  var font_size = Math.floor(size/5).toString();
  ctx.font = font_size.concat("px Arial");
  var x_dict = {
    0: size/10,
    1: size/2.3, 
    2: size/1.3, 
  };
  var y_dict = {
    0: size/4,
    1: size/1.8,
    2: size/1.15,
  };
  ctx.fillText(letter, x_dict[x], y_dict[y]);
}
