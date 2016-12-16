# DO NOT MODIFY THIS FILE.

class RavensObject:

    def __init__(self, name):
        # The name of this RavensObject. Names are assigned starting with the
        # letter Z and proceeding backwards in the alphabet through the objects
        # in the Frame. Names do not imply correspondence between shapes in
        # different frames. Names are simply provided to allow agents to organize
        # their reasoning over different figures.
        #
        # Within a RavensFigure, each RavensObject has a unique name.
        self.name=name

        # A dictionary of name-value pairs representing this object's attributes. The key
        # for these attributes is the name of the attribute, and the value is the
        # value of the attribute. For example, a filled large square would have
        # attribute pairs "shape:square", "size:large", and "filled:yes".
        self.attributes={}

