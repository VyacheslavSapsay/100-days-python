# class Segment:
#     def __init__(self, x_cor, y_cor):
        

from turtle import Turtle

class Snake:
    STARTING_SEGMENTS_COUNT = 3
    SEGMENT_SIZE = 20
    TURNING_SETTINGS = {
        'Up': 90,
        'Down': 270,
        'Right': 0,
        'Left': 180
    }
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setposition(new_x, new_y)
    
        self.segments[0].forward(20)
    
    def create_snake(self):
        for i in range(self.STARTING_SEGMENTS_COUNT):
            self.add_segment()
    
    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.resizemode('user')
        new_segment.penup()
            
        if len(self.segments) > 0:
            prev_segment_pos = self.segments[-1].position()
            new_position = prev_segment_pos[0] - self.SEGMENT_SIZE, prev_segment_pos[1]
            new_segment.setposition(new_position)
                
        self.segments.append(new_segment)
    
    def up(self):
        if self.head.heading() != self.TURNING_SETTINGS['Down']:
            self.segments[0].setheading(self.TURNING_SETTINGS['Up'])
    
    def down(self):
        if self.head.heading() != self.TURNING_SETTINGS['Up']:
            self.segments[0].setheading(self.TURNING_SETTINGS['Down'])
    
    def right(self):
        if self.head.heading() != self.TURNING_SETTINGS['Left']:
            self.segments[0].setheading(self.TURNING_SETTINGS['Right'])
    
    def left(self):
        if self.head.heading() != self.TURNING_SETTINGS['Right']:
            self.segments[0].setheading(self.TURNING_SETTINGS['Left'])
        