# spots_model.py
#
# ICS 32 Winter 2014
# Code Example
#
# This module consists of a model for our Spots application.  The
# model is embodied, primarily, in a class called SpotsState.  A running
# instance of our Spots application contains one SpotsState object that
# represents, collectively, the application's state (i.e., the list of
# spots that currently exist).
#
# Each spot is itself represented as a Spot object, which know enough to
# allow us to easily manipulate and draw them.

import coordinate



# This constant specifies the radius, in fractional coordinates, of the
# spots that are created.  Try changing this to be larger or smaller and
# see what happens.
SPOT_RADIUS_FRAC = 0.05



class Spot:
    def __init__(self, center: coordinate.Coordinate, radius_frac: float):
        '''
        Initialize a newly-created Spot object, given its center
        coordinate (a Coordinate object) and the spot's radius (in
        fractional coordinates).
        '''
        self._center = center
        self._radius_frac = radius_frac


    def center_coordinate(self) -> coordinate.Coordinate:
        '''
        Returns a Coordinate object representing this Spot's
        center coordinate.
        '''
        return self._center


    def radius_frac(self):
        '''
        Returns the radius of this Spot, in terms of fractional
        coordinates.
        '''
        return self._radius_frac


    def contains(self, coordinate: coordinate.Coordinate) -> bool:
        '''
        Returns True if the given Coordinate object lies within
        this Spot, False otherwise.
        '''

        # Since Coordinate objects know how to calculate a distance
        # between themselves and other Coordinate objects, all we
        # need to do is ask the center coordinate how far it is
        # from the given coordinate; if that's less than or equal
        # to the radius, the given coordinate is within the spot.
        return self._center.frac_distance_from(coordinate) <= self._radius_frac
    


class SpotsState:
    def __init__(self):
        '''
        Initializes the state of the Spots application.  Initially,
        there are no spots.
        '''
        self._spots = []


    def all_spots(self) -> [Spot]:
        '''Returns a list of all of the Spot objects that currently exist.'''
        return self._spots


    def handle_click(self, click_coordinate: coordinate.Coordinate) -> None:
        '''
        Handle a click on the given coordinate, by either removing the
        spot in which the coordinate lies, or by adding a new spot centered
        at the given coordinate.
        '''

        # Spot objects are stored in the order they've been created,
        # newer ones appearing later in the list than earlier ones.
        # We'll scan the list of spots backward looking for an existing
        # spot that contains the given coordinate, so we'll match newer
        # spots when given a choice.  This is important, because newer
        # spots are drawn on top of older ones.
        #
        # Note, too, how simple this loop is.  Most of the hard stuff
        # -- conversions between coordinate systems, figuring out whether
        # a click lies within a particular spot -- is already handled in
        # other places.  When we've fashioned ourselves the right tools,
        # we can build other code in terms of those tools.

        for i in reversed(range(len(self._spots))):
            if self._spots[i].contains(click_coordinate):
                # Once we find a match, delete it and we're done.
                del self._spots[i]
                return

        # If we got out of the loop, we never found a match, so we'll
        # instead create a new spot, centered where the click occurred.
        self._spots.append(Spot(click_coordinate, SPOT_RADIUS_FRAC))
