var my_canvas = document.getElementById("myCanvas");
my_canvas.onload = ttt_loader();
var w = window.innerWidth;
var h = window.innerHeight;
var size = Math.min(w*0.66, h*0.66);
var my_board = [[0,0,0],[0,0,0],[0,0,0]];
var latest_move = "";

function ttt_loader() {
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
  my_canvas.addEventListener('click', ttt_click, false);

  // Add event listener for `onmouseover` events. Will add this feature later.
  //my_canvas.addEventListener('mouseover', ttt_hover, false);  
}

function ttt_click(event) {
    var ctx = my_canvas.getContext("2d");
    var x = event.pageX - (w-size)/2,
        y = event.pageY - (h-size)/2;
    var move = [Math.floor(y/(size/3)),Math.floor(x/(size/3))];
    if (my_board[move[0]][move[1]]===0) {
      //alert(check_board(my_board));
      if (check_board(my_board)) {
        draw_letter(ctx, "X", move[1], move[0]);
        my_board[move[0]][move[1]] = 1;
      }
      //alert(check_board(my_board));
      if (check_board(my_board)) {
        var computer_move = get_move(my_board);
        draw_letter(ctx, "O",computer_move[1],computer_move[0]);
        my_board[computer_move[0]][computer_move[1]] = -1;
      }
      check_board(my_board);
    }
}

function check_board(board, ctx) {
  var winner = 0;
  var ctx = my_canvas.getContext("2d");
  for (var i=0; i<3; i++) {
    if (board[i][0]===board[i][1]&&board[i][1]===board[i][2]&&board[i][2]!=0) {
      winner = board[i][0];
    }
  }
  for (i=0; i<3; i++) {
    if (board[0][i]===board[1][i]&&board[1][i]===board[2][i]&&board[2][i]!=0) {
      winner = board[0][i];
    }
  }
  if (board[0][0]===board[1][1]&&board[1][1]===board[2][2]&&board[2][2]!=0) {
    winner = board[0][0];
  }
  if (board[0][2]===board[1][1]&&board[1][1]===board[2][0]&&board[2][0]!=0) {
    winner = board[0][2];
  }
  //alert(board);
  //alert(winner);
  if (winner === 0) {
    return true;
  } else {
    my_canvas.removeEventListener('click', ttt_click);
    //setTimeout(function(){ ttt_loader(); my_board = [[0,0,0],[0,0,0],[0,0,0]];}, 3000);
    my_board = [[0,0,0],[0,0,0],[0,0,0]];
    return false;
  }
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

function get_move(board) {
  var moves = [];
  for (var i=0; i<board.length; i++) {
    for (var j=0; j<board[i].length; j++) {
      if (board[i][j]===0) {
        moves.push([i,j]);
      }
    }
  }
  var selected = Math.floor(Math.random()*moves.length);
  var move = moves[selected];
  return move;
}