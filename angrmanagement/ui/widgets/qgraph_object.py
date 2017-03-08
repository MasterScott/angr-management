
from PySide.QtGui import QPainter


class QGraphObject(object):
    def __init__(self):

        self._x = None
        self._y = None
        self._width = None
        self._height = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def pos(self):
        """

        :return:
        """

        return self.x, self.y

    def size(self):
        """

        :return:
        """

        return self.width, self.height

    def paint(self, painter):
        """

        :param QPainter painter: The painter object.
        :return:                 None
        """

        raise NotImplementedError()

    def on_mouse_pressed(self, button, pos):
        """

        :param button:
        :param pos:
        :return:
        """

        pass