# Solomon Chan, Lab 6)
# I certify that I written all the code in this programming assignment 
# by myself.
import controller, sys
#import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special 

from prey import Prey


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
selected_object = None
world_objects = []



#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, selected_object, world_objects
    running = False
    cycle_count = 0
    selected_object = None
    world_objects = []


#start running the simulation
def start ():
    global running
    running = True
    print('start')


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running
    running = True
    update_all()
    running = False
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global selected_object
    selected_object = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global world_objects, selected_object
    if selected_object != "Remove" and selected_object != "None":
        add(eval("{}({}, {})".format(selected_object, x, y)))
    elif selected_object == "Remove":
        for item in world_objects:
            if item.contains((x,y)):
                remove(item)



#add simulton s to the simulation
def add(s):
    global world_objects
    #s.display(controller.the_canvas)
    world_objects.append(s)
    print("Added a {} object".format(str(s)))

# remove simulton s from the simulation    
def remove(s):
    global world_objects
    #s.display(controller.the_canvas)
    world_objects.remove(s)
    print('remove')

def remove_all(objects):
    for obj in objects:
        remove(obj)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    global world_objects
    for element in world_objects:
        if p(element):
            result.add(element)
    return result
        


#call update for every simulton in the simulation
def update_all():
    global cycle_count,running,world_objects
    
    if running:
        cycle_count += 1
        to_remove = set()
        
        for obj in world_objects:
            if isinstance(obj,Black_Hole):
                eaten = obj.update(lambda x: isinstance(x,Prey))
                for thing in eaten:
                    to_remove.add(thing)
            else:
                obj.update()
        
        remove_all(to_remove)

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    global world_objects
    for pixel in controller.the_canvas.find_all():
        controller.the_canvas.delete(pixel)
    
    for obj in world_objects:
        obj.display(controller.the_canvas)
    controller.the_progress.config(text=str(len(world_objects))+" updates/"+str(cycle_count)+" cycles")