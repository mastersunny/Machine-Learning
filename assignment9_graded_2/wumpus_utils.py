from ipycanvas import RoughCanvas, hold_canvas

canvas = RoughCanvas(width=200, height=200)

def draw_world(wumpus_world, agent_pos=None):
    with hold_canvas(canvas):
        canvas.clear()

        # the cells
        for r in range(wumpus_world.shape[0]):
            for c in range(wumpus_world.shape[1]):
                canvas.stroke_rect(c*50, r*50, 50, 50)

        # the content
        canvas.font = '32px serif'
        canvas.text_align = 'center'
        for r in range(wumpus_world.shape[0]):
            for c in range(wumpus_world.shape[1]):
                if agent_pos is not None and r == agent_pos[0] and c == agent_pos[1]:
                    if wumpus_world[r][c] == "W" or wumpus_world[r][c] == "P" or wumpus_world[r][c] == "G": # is in end position
                        canvas.fill_text("X", c*50+25, r*50+25 + 8)
                    else:
                        canvas.fill_text("A", c*50+25, r*50+25 + 8)
                else:
                    if not wumpus_world[r][c] == "E":
                        canvas.fill_text(wumpus_world[r][c], c*50+25, r*50+25 + 8)

def display_world():
    display(canvas)