
class Bishop:
    @staticmethod
    def get_moves(cord, piece, chess_board):
        """
        :param cord:            row and column of piece on board
        :param piece:           instance of the piece's object class
        :param chess_board:     the chessboard the pieces are on
        :return:
        """
        valid_locs = []
        r, c = cord[0], cord[1]

        # Loop to add spaces below and to the right of the bishop
        for off in range(1, 8):
            new_r = r + off
            new_c = c + off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break
            # if the chessboard holds None (no other piece) then add right and down direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces above and to the right of the bishop
        for off in range(1, 8):
            new_r = r - off
            new_c = c + off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            # if the chessboard holds None (no other piece) then add left and down direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces below and to the left of the bishop
        for off in range(1, 8):
            new_r = r + off
            new_c = c - off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break
            # if the chessboard holds None (no other piece) then add right and up direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        # Loop to add spaces above and to the left of the bishop
        for off in range(1, 8):
            new_r = r - off
            new_c = c - off

            # if the offset pushes the piece off the board brake out
            if new_r > 7 or new_c > 7 or new_r < 0 or new_c < 0:
                break

            # if the chessboard holds None (no other piece) then add left and up direction
            if chess_board[(new_r, new_c)] is None:
                valid_locs.append((new_r, new_c))
            else:
                # append location if enemy can be captured
                if chess_board.is_enemy((new_r, new_c), piece):
                    valid_locs.append((new_r, new_c))
                break

        return valid_locs
