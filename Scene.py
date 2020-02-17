from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsSceneMouseEvent
from NewRectangle import newRectangle
from PyQt5.QtCore import Qt, QRectF, pyqtSignal, QObject
from PyQt5.QtGui import QPen


class Scene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.draw = False
        self.m_left_btn_press = False
        self.m_items = []
        self.rect = QGraphicsRectItem()
        self.lastPos_X = 0
        self.lastPos_Y = 0
        # self.onResize = pyqtSignal()

    def set_draw_enable(self, en):
        self.draw = en
        items_list = self.items()
        for item in items_list:
            if isinstance(item, newRectangle):
                if self.draw:
                    item.setMovable(False)
                else:
                    item.setMovable(True)

    def isDrawEnable(self):
        return self.draw

    def lastPosition_X(self):
        return self.lastPos_X

    def lastPosition_Y(self):
        return self.lastPos_Y

    def getCutRegions(self):
        items_list = self.items()
        self.m_items.clear()
        for item in items_list:
            if isinstance(item, newRectangle):
                # код с CV
                pass  # временно
        return self.m_items

    def sortSizeRect(self):
        list = []
        items_list = self.items()
        for item in items_list:
            if isinstance(item, newRectangle):
                list.append(item)
        sorted(list, key=lambda a, b: a.get_W() * a.get_H < b.get_W() * b.get_H())
        for i in list:
            list[i].setZValue(1000 - i)

    def deleteItem(self):
        items_list = self.items()
        count = 0
        for item in items_list:
            if isinstance(item, newRectangle):
                if (item.isSelected()):
                    self.removeItem(item)
                    count += 1
        if count > 0:
            self.update()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        super().mousePressEvent(event)
        if self.draw:
            if event.button() == Qt.LeftButton:
                self.rect.setRect(QRectF(event.scenePos().x(), event.scenePos().y(), 0, 0))
                self.rect.setPen(QPen(Qt.red, 2))
                self.addItem(self.rect)

                self.lastPos_X = event.scenePos().x()
                self.lastPos_Y = event.scenePos().y()
                self.m_left_btn_press = True

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent):
        super().mouseMoveEvent(event)
        rectangle = QRectF()
        if self.draw:
            if self.m_left_btn_press:
                lastPos_X = self.lastPosition_X()
                lastPos_Y = self.lastPosition_Y()
                if event.scenePos().x() > lastPos_X and event.scenePos().y() > lastPos_Y:
                    rectangle.setTopLeft(self.rect.rect().topLeft())
                    rectangle.setBottomRight(event.scenePos())
                    self.rect.setRect(rectangle)

                elif event.scenePos().x() < lastPos_X and event.scenePos().y() > lastPos_Y:
                    rectangle.setTopRight(self.rect.rect().topRight())
                    rectangle.setBottomLeft(event.scenePos())
                    self.rect.setRect(rectangle)

                elif event.scenePos().x() < lastPos_X and event.scenePos().y() < lastPos_Y:
                    rectangle.setBottomRight(self.rect.rect().bottomRight())
                    rectangle.setTopLeft(event.scenePos())
                    self.rect.setRect(rectangle)

                elif event.scenePos().x() > lastPos_X and event.scenePos().y() < lastPos_Y:
                    rectangle.setBottomLeft(self.rect.rect().bottomLeft())
                    rectangle.setTopRight(event.scenePos())
                    self.rect.setRect(rectangle)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent):
        super().mousePressEvent(event)
        if self.draw:
            if event.button() == Qt.LeftButton:
                initRect = QRectF(self.rect.rect())
                self.removeItem(self.rect)
                self.nrect = newRectangle(initRect)
                self.nrect.onResizeSignal.connect(self.sortSizeRect)
                self.nrect.setMovable(False)
                self.addItem(self.nrect)
                self.m_left_btn_press = False
                self.sortSizeRect()
