def compose(notes, moves, start):
    position = start
    song = [notes[position]]
    for move in moves:
        position = (position + move) % len(notes)
        song.append(notes[position])
    return song

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
