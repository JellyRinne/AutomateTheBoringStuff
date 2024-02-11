import pprint

validBoard = {'1h': 'bking',
              '6c': 'wqueen',
              '2g': 'bbishop',
              '5h': 'bqueen',
              '3e': 'wking',
              '4h': 'bpawn',
              '6g': 'wpawn'}

invalidBoard1 = {'1h': 'bking',
                '6c': 'wqueen',
                '2p': 'bbishop',
                '5h': 'wking',
                '3g': 'brook'}

invalidBoard2 = {'1h': 'wqueen',
                '6c': 'wknight',
                '2g': 'bbishop',
                '5h': 'wking',
                '3a': 'bpawn',
                '3b': 'bpawn',
                '3c': 'bpawn',
                '3d': 'bpawn',
                '3e': 'bpawn',
                '3f': 'bpawn',
                '3g': 'bpawn',
                '3h': 'bpawn',
                '4e': 'bpawn',
                '5e': 'bpawn',
                '6e': 'bpawn',
                '7e': 'bpawn',
                '8e': 'bpawn',}
                

invalidBoard3 = {'1h': 'bking',
                '6c': 'wqueen',
                '9g': 'bgeorge',
                '5h': 'wking',
                '3e': 'wking'}

def isValidChessBoard(board):
    try:
        validVertical = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        validHorizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        validPieceNames = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        counts = {'bpieces': 0,
                  'wpieces': 0,
                  'bpawns': 0,
                  'wpawns': 0,
                  'wvalidspaces': True,
                  'bvalidspaces' : True,
                  'bnames': True,
                  'wnames': True}

        for k, v in board.items():
            if v[0] == 'b':
                counts['bpieces'] += 1
            if v[0] == 'w':
                counts['wpieces'] += 1
            if v == 'bpawn':
                counts['bpawns'] += 1
            if v == 'wpawn':
                counts['wpawns'] += 1
            if v[1:len(v)] not in validPieceNames and v[0] == 'b':
                counts['bnames'] = False
            if v[1:len(v)] not in validPieceNames and v[0] == 'w':
                counts['wnames'] = False
            if (v[0] == 'b' and k[0] not in validVertical) or (v[0] == 'b' and k[1] not in validHorizontal):
                counts['bvalidspaces'] = False
            if (v[0] == 'w' and k[0] not in validVertical) or (v[0] == 'w' and k[1] not in validHorizontal):
                counts['wvalidspaces'] = False
    
        if counts['bpieces'] > 16 or counts['wpieces'] > 16 or counts['bpawns'] > 8 or counts['wpawns'] > 8 or counts['bnames'] == False or counts['wnames'] == False or counts['bvalidspaces'] == False or counts['wvalidspaces'] == False:
            return False
        else:
            return True
    except:
        print('Oops! Encountered an error!')

print('::::::::Board Evals::::::::')

print()

pprint.pprint(validBoard)
if isValidChessBoard(validBoard):
    print('Board is Valid.')
else:
    print('Board is Invalid.')

print()

pprint.pprint(invalidBoard1)
if isValidChessBoard(invalidBoard1):
    print('Board is Valid.')
else:
    print('Board is Invalid.')

print()

pprint.pprint(invalidBoard2)
if isValidChessBoard(invalidBoard2):
    print('Board is Valid.')
else:
    print('Board is Invalid.')

print()

pprint.pprint(invalidBoard3)
if isValidChessBoard(invalidBoard3):
    print('Board is Valid.')
else:
    print('Board is Invalid.')