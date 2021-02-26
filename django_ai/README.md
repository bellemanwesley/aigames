# AI Games Web Server

This directory is dedicated to the web server front end for the website. Below I have documented all of the HTTP requests made between the client and the web server. The web server is written with Django.

## URLs
The AIGames web server has three URLs:
   - `/`: home page
   - `/tictactoe`: tic-tac-toe game
   - `/checkers`: checkers game

## /

## /tictactoe

```
    POST /tictactoe
        {
            "csrfmiddlewaretoken": csrf_token,
            "board": board_string
        }
```

## /checkers