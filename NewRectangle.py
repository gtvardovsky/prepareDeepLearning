from PyQt5.QtCore import QObject, QRectF, Qt, pyqtSignal
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QPen
import copy

RESIZE_ZONE_SIZE = 5;
MIN_AREA_SIZE = 10;

class newRectangle(QGraphicsItem):
    def __init__(self, initialRect):
        super().__init__()
        self.m_innerRect = initialRect
        # Нахождение мыши: True  - внутри прямоугольника, False - вне
        self.m_hovered = False
        # Разрешение на выбор, перемещение или ресайз прямоугольника
        self.m_movable = True
        # Текущее действие: предвижение, ресайз
        self.m_active_zone = None
        # Без этого не будет работать hoverEnterEvent() и hoverLeaveEnter()
        self.setAcceptHoverEvents(True)
        # Флаг для разрешения "выбора" прямоугольника
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        # Аналог emit() из Qt creator
        #self.onResize_signal = pyqtSignal()


    # Определение (пересчет) рабочей (кликабельной) зоны для прямоугольника
    def boundingRect(self):
        return QRectF(
            self.m_innerRect.left() - RESIZE_ZONE_SIZE / 2.0,
            self.m_innerRect.top() - RESIZE_ZONE_SIZE / 2.0,
            self.m_innerRect.width() + RESIZE_ZONE_SIZE,
            self.m_innerRect.height() + RESIZE_ZONE_SIZE
        )

    # Отрисовка прямоугольника и квадратиков по углам
    def paint(self, painter, option, widget):
        # Настраиваем "карандаш"
        m_pen = QPen(Qt.red)
        m_pen.setWidth(3)
        painter.setPen(m_pen)
        # Рисуем прямоугольник
        painter.drawRect(self.m_innerRect)

        # Проверяем кликнут ли прямоугольник для отрисовки квадратиков по углам
        if self.isSelected():
            zones = self.generate_zones()
            for key in zones:
                painter.fillRect(zones[key], Qt.white)
                painter.drawRect(zones[key])

    # Событие входа курсора мышми в область прямоугольника
    def hoverEnterEvent(self, event):
        self.m_hovered = True
        # Неявный вызов paint() для перерисовки
        self.update()
        if self.isSelected():
            self.setCursor(Qt.OpenHandCursor)

    # Событие выхода курсора мышми из области прямоугольника
    def hoverLeaveEvent(self, event):
        self.m_hovered = False
        self.update()
        self.setCursor(Qt.ArrowCursor)

    # Событие нажатия клавиши мыши
    def mousePressEvent(self, event):
        if self.m_movable:
            self.scene().clearSelection()
            self.setSelected(True)
            if event.button() == Qt.LeftButton:
                zones = self.generate_zones()
                for key in zones:
                    if zones[key].contains(event.pos()):
                        self.m_active_zone = key
                        break
                if self.m_active_zone == 'RESIZE_TOP_LEFT_ZONE' or self.m_active_zone == 'RESIZE_TOP_RIGHT_ZONE' or\
                    self.m_active_zone == 'RESIZE_BOTTOM_LEFT_ZONE' or self.m_active_zone == 'RESIZE_BOTTOM_RIGHT_ZONE' :
                    self.setCursor(Qt.PointingHandCursor)
                else:
                    self.setCursor(Qt.ClosedHandCursor)
                if self.m_active_zone is None and self.m_innerRect.contains(event.pos()):
                    self.m_active_zone = "MOVE_ZONE"
                    self.m_center_offset = event.pos() - self.m_innerRect.center()
            elif event.button() == Qt.RightButton:
                pass

    # Событие движения мыши
    def mouseMoveEvent(self, event):
        if self.m_movable:
            self.prepareGeometryChange()
            if self.scene():
                sRect = self.scene().sceneRect()
                # Если двигаем прямоугольник, то перемещаем его за коородинатами мыши
                if self.m_active_zone == "MOVE_ZONE":
                    self.setCursor(Qt.ClosedHandCursor)
                    self.m_innerRect.moveCenter(event.pos() - self.m_center_offset)

                    if self.m_innerRect.left() < sRect.left():
                        self.m_innerRect.moveLeft(sRect.left())

                    if self.m_innerRect.top() < sRect.top():
                        self.m_innerRect.moveTop(sRect.top())

                    if sRect.right() < self.m_innerRect.right():
                        self.m_innerRect.moveRight(sRect.right())

                    if sRect.bottom() < self.m_innerRect.bottom():
                        self.m_innerRect.moveBottom(sRect.bottom())

                elif self.m_active_zone == "RESIZE_TOP_LEFT_ZONE":
                    self. m_innerRect.setTopLeft(event.pos())

                elif self.m_active_zone == "RESIZE_TOP_RIGHT_ZONE":
                    self.m_innerRect.setTopRight(event.pos())

                elif self.m_active_zone == "RESIZE_BOTTOM_LEFT_ZONE":
                    self.m_innerRect.setBottomLeft(event.pos())

                elif self.m_active_zone == "RESIZE_BOTTOM_RIGHT_ZONE":
                    self.m_innerRect.setBottomRight(event.pos())

                if self.m_active_zone is not None:
                    if self.m_innerRect.left() < sRect.left():
                        self.m_innerRect.setLeft(sRect.left())

                    if self.m_innerRect.top() < sRect.top():
                        self.m_innerRect.setTop(sRect.top())

                    if sRect.right() < self.m_innerRect.right():
                        self.m_innerRect.setRight(sRect.right())

                    if sRect.bottom() < self.m_innerRect.bottom():
                        self.m_innerRect.setBottom(sRect.bottom())

                    # Ограничение минимального размера квадрата
                    if self.m_innerRect.width() < MIN_AREA_SIZE:
                        if self.m_active_zone == "RESIZE_BOTTOM_LEFT_ZONE" or self.m_active_zone == "RESIZE_TOP_LEFT_ZONE":
                            self.m_innerRect.setLeft(self.m_innerRect.right() - MIN_AREA_SIZE)
                        else:
                            self.m_innerRect.setRight(self.m_innerRect.left() + MIN_AREA_SIZE)

                    if self.m_innerRect.height() < MIN_AREA_SIZE:
                        if self.m_active_zone == "RESIZE_TOP_LEFT_ZONE" or self.m_active_zone == "RESIZE_TOP_RIGHT_ZONE":
                            self.m_innerRect.setTop(self.m_innerRect.bottom() - MIN_AREA_SIZE)
                        else:
                            self.m_innerRect.setBottom(self.m_innerRect.top() + MIN_AREA_SIZE)

    # Событие "отпускания" клавиши мыши
    def mouseReleaseEvent(self, event):
        if self.m_movable:
            self.m_active_zone = None
            self.setCursor(Qt.OpenHandCursor)
            #self.onResize.emit()

    # Генерация координат квадратиков по углам
    def generate_zones(self):
        zoneRect = QRectF(0,0, RESIZE_ZONE_SIZE, RESIZE_ZONE_SIZE)
        zoneCenters = {}
        zoneCenters['RESIZE_TOP_LEFT_ZONE'] = self.m_innerRect.topLeft()
        zoneCenters['RESIZE_TOP_RIGHT_ZONE'] = self.m_innerRect.topRight()
        zoneCenters['RESIZE_BOTTOM_LEFT_ZONE'] = self.m_innerRect.bottomLeft()
        zoneCenters['RESIZE_BOTTOM_RIGHT_ZONE'] = self.m_innerRect.bottomRight()
        zones = {}
        for key in zoneCenters.keys():
            zoneRect.moveCenter(zoneCenters[key])
            zones[key] = copy.copy(zoneRect)
        return zones

    def setMovable(self, en):
        self.m_movable = en
        if en:
            self.setAcceptHoverEvents(True)
            self.setFlag(QGraphicsItem.ItemIsSelectable)
            self.setFlag(QGraphicsItem.ItemIsMovable)
        else:
            self.setAcceptHoverEvents(False)
            self.setFlag(QGraphicsItem.ItemIsSelectable, False)
            self.setFlag(QGraphicsItem.ItemIsMovable, True)

    def get_W(self):
        return self.m_innerRect.width()

    def get_H(self):
        return self.m_innerRect.height()

