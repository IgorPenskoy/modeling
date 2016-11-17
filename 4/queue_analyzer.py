#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random
import math
from PyQt5.uic import loadUiType

Ui_MainWindow, QMainWindow = loadUiType('gui.ui')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.method = 0
        self.stop_condition = 0
        self.dt_radio.clicked.connect(self.set_method_dt)
        self.event_radio.clicked.connect(self.set_method_event)
        self.requestcount_radio.clicked.connect(self.set_stop_condition_requestcount)
        self.time_radio.clicked.connect(self.set_stop_condition_time)
        self.run_button.clicked.connect(self.calculate_optimal_queue_length)

    def set_method_dt(self):
        self.dt_label.setEnabled(True)
        self.dt_spin.setEnabled(True)
        self.stats_label.setEnabled(False)
        self.stats_spin.setEnabled(False)
        self.method = 0

    def set_method_event(self):
        self.dt_label.setEnabled(False)
        self.dt_spin.setEnabled(False)
        self.stats_label.setEnabled(True)
        self.stats_spin.setEnabled(True)
        self.method = 1

    def set_stop_condition_requestcount(self):
        self.requestcount_spin.setEnabled(True)
        self.time_spin.setEnabled(False)
        self.stop_condition = 0

    def set_stop_condition_time(self):
        self.requestcount_spin.setEnabled(False)
        self.time_spin.setEnabled(True)
        self.stop_condition = 1

    def double_spinbox_to_float(self, spinbox):
        return float(str(spinbox.text()).replace(',','.'))

    def uniform_gen(self, a, b):
        return a + (b - a) * random.random()

    def normal_gen(self, mu, sigma):
        s = 0
        for i in range(12):
            s += random.random()
        return mu + (s - 6) * sigma

    def dt_requestcount(self, dt, request_count, a, b, mu, sigma, p_return):
        optimal_length = 1
        current_length = 1
        current_size = 0
        t = 0
        denial = 1
        while denial != 0:
            denial = 0
        return optimal_length


    def dt_time(self, dt, time, a, b, mu, sigma, p_return):
        optimal_length = 1
        current_length = 1
        current_size = 0
        t = 0
        denial = 1
        while denial != 0:
            denial = 0
        return optimal_length

    def event_requestcount(self, stats, request_count, a, b, mu, sigma, p_return):
        optimal_length = 1
        current_length = 1
        current_size = 0
        t = 0
        denial = 1
        while denial != 0:
            denial = 0
        return optimal_length

    def event_time(self, stats, time, a, b, mu, sigma, p_return):
        optimal_length = 1
        current_length = 1
        current_size = 0
        t = 0
        denial = 1
        while denial != 0:
            denial = 0
        return optimal_length



    def calculate_optimal_queue_length(self):
        a = self.double_spinbox_to_float(self.a_spin)
        b = self.double_spinbox_to_float(self.b_spin)
        mu = self.double_spinbox_to_float(self.mu_spin)
        sigma = self.double_spinbox_to_float(self.sigma_spin)
        possibilty_return = self.double_spinbox_to_float(self.return_spin)
        dt = self.double_spinbox_to_float(self.dt_spin)
        stat_time = self.double_spinbox_to_float(self.stats_spin)
        request_count = self.double_spinbox_to_float(self.requestcount_spin)
        time = self.double_spinbox_to_float(self.time_spin)
        if self.method == 0:
            if self.stop_condition == 0:
                optimal_length = self.dt_requestcount(dt, request_count, a, b, mu, sigma, possibilty_return)
            else:
                optimal_length = self.dt_time(dt, time, a, b, mu, sigma, possibilty_return)
        else:
            if self.stop_condition == 0:
                optimal_length = self.event_requestcount(stat_time, request_count, a, b, mu, sigma, possibilty_return)
            else:
                optimal_length = self.event_time(stat_time, time, a, b, mu, sigma, possibilty_return)
        self.optimal_label.setText('Оптимальная длина очереди: ' + str(optimal_length))


if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
    import PyQt5
    import numpy as np
    random.seed()
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())