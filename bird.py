class Bird(object):
    """ The Bird class variables:
            1. position is a tuple with the (x, y) coordinates of the bird 
            2. previous_position is the position in the previous time step
    """
    def __init__(self, position):
        self.position = position
        self.previous_position = position
        return

    def move(self):
        #The move function will move the bird
        return
    
    def is_too_close(self, other_bird, minimum_separation):
        #Checks if the bird is too close to another bird
        if (other_bird.position[0] - self.position[0])**2 + \
                (other_bird.position[1] - self.position[1])**2 < minimum_separation**2:
            return True
        else:
            return False
            

            

                                                                    

    

