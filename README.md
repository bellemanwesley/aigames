aigames
========

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

AIGames is a website located at http://aigames.wkbonline.net/. The website 

Installation instructions
-------------------------

    git clone https://github.com/bellemanwesley/aigames.git
    cd aigames
    sh setup.sh
    sh run.sh

## URLs
The AIGames web server has three URLs:
   - `/`: home page
   - `/tictactoe`: tic-tac-toe game
   - `/checkers`: checkers game

# bitfold

*import statebasedml.bitfold*

```python
	from statebasedml import bitfold
```

*bitfold has 2 methods*
   - `gen_param()`: generates the parameters for a fold
   - `fold()`: actually folds the input data

## gen_param

*request syntax*

```python

    fold_parameters = bitfold.gen_param(
        size = 256
    )

```

```
    POST /tictactoe
        {
            "csrfmiddlewaretoken": csrf_token,
            "board": board_string
        }
```