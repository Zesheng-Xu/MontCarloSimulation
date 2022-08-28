import math

import matplotlib.pyplot as plt
import numpy as np
import numpy.random



class Simulation():
    def __init__(self,trial_num =1, points_num =30,radius = np.random.uniform(5,10), headless = False, in_plt=plt ):
        """
        :param trial_num: int
            numbers of trials to run
        :param points_num: int
            numbers of points to plot
        :param radius: float
            to determine the size of rectable and circle
        :param headless: bool
            determine to display plotting process or not
        :param in_plt: matplotlib.pyplot
            plot to draw on
        """
        self.plt = in_plt
        self.trial_nums = trial_num
        self.points_num = points_num
        self.radius = radius
        self.headless = headless
    def drawCircle(self,graph: plt,radius:float):
        """
        Draw a circle on given plot
        :param graph:  mpl.pyplot
            The plot board to draw the circle on
        :param radius: float
            radius of a circle
        :return:
        """
        circle = plt.Circle((self.radius,self.radius), radius, fc = "blue", ec = "black" )
        graph.gca().add_patch(circle)
        graph.axis('scaled')

        return


    def drawSquare(self,graph: plt,length:float):
        """
        Draw a circle on given plot
        :param graph:  mpl.pyplot
            The plot board to draw the circle on
        :param length: float
            length of the sides of a square
        :return:
        """
        rectangle = plt.Rectangle((0, 0), length, length, fc='white', ec="black")
        graph.gca().add_patch(rectangle)
        graph.axis('scaled')

        return
    def withInCircle(self,point, radius):
        """
        Check if the input point is within circle
        :param point: list[int]
            contains 2 numbers: x and y of the point
        :param radius: float
            radious of the circle
        :return: boolean
            True of inside circle, else False
        """
        if (point[0]-self.radius)**2 + (point[1]-self.radius)**2 <= radius **2:
            return True
        else:
            return False
    def run(self):
        """
        Runs the simulation and return result
        :return:
        """

        import time
        predicted_PI = 0
        total_points = 0
        points_in = 0



        result = [0.0]*self.trial_nums
        # exampel 30 trials for this many number of points
        if not self.headless:
            self.plt.ion()
            self.plt.show()
        for i in range(0,self.trial_nums):
            if not self.headless:
                self.drawSquare(self.plt,self.radius*2)
                self.drawCircle(self.plt,self.radius)
            if not self.headless:

                plt.title("PI Estimation Using Monte Carlo Method")
                tp_text = self.plt.text(-self.radius/1.5 - 0.75, 1.75 * self.radius + (0.6) * self.radius, f"Total points: {total_points}", fontsize=10, )
                pi_text = self.plt.text(-self.radius/1.5 - 0.75, 1.75 * self.radius + (0.5) * self.radius, f"Points inside the circle: {points_in}", fontsize=10, )
                pp_text = self.plt.text(-self.radius/1.5 - 0.75, 1.75 * self.radius + (0.4) * self.radius, f"Predicted_PI: {predicted_PI}", fontsize=10, )
            for j in range(0,self.points_num):
                point = [0,0]
                point[0] = numpy.random.uniform(0,self.radius * 2)
                point[1] = numpy.random.uniform(0,self.radius * 2)
                if not self.headless:
                    plt.scatter(point[0],point[1])
                total_points += 1

                if self.withInCircle(point, self.radius):
                    points_in += 1
                predicted_PI = points_in/total_points * 4
                if not self.headless:
                    tp_text.set_text(f"Total points: {total_points}")
                    pi_text.set_text(f"Points inside the circle: {points_in}")
                    pp_text.set_text(f"Predicted_PI: {round(predicted_PI,2)}")
                    self.plt.pause(0.05)
                    time.sleep(0.1)
            if not self.headless:
                self.plt.clf()
            result[i] = predicted_PI
            predicted_PI = 0
            total_points = 0
            points_in = 0

        return result

