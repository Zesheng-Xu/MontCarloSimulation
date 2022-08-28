"""
How does this simulation work:
    We draw a square with side length 2* r, and a circle inside it with radius r.
    Area of the square = (2 * r)^2 =4 * r^2
    Area of the circle =  PI * r^2

    Theoretically when we place a number of dots on to the plot:
        There are (1/2 * PI * r^2 ) / (4 * r^2 ) chance that the point will be inside the circle.
        From their percentage we can approximate value of PI.
            percent / probability(points in circle) = (1/2 * PI * r^2 ) / (4 * r^2 )
            numbers of point in circle / total points plotted = 1/4 * PI
            PI = 48 * numbers of point in circle / total points plotted

"""
import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.random
import pandas as pd

from Simulation import Simulation

if __name__ == "__main__":
    output = "output"
    actual_pi = math.pi

    points_num = 100
    num_trials = 500
    num_point_arr = [x for x in range(1, points_num + 1)]
    pp_arr = [0] * points_num  # predicted Pi value
    ppp_arr = [0] * points_num  # profit per point

    for i in range(1, points_num + 1):
        sim = Simulation(trial_num=10, points_num=i, radius=np.random.uniform(5, 10), headless=False, in_plt=plt)
        data = sim.run()
        data_avg = abs(sum(data) / len(data))
        accuracy = abs(data_avg - actual_pi)
        profit_per_point = accuracy / i
        pp_arr[i - 1] = abs(sum(data) / len(data))
        ppp_arr[i - 1] = profit_per_point
    pp_df = pd.DataFrame({"Number of points": num_point_arr, "Predicted PI": pp_arr})  # predicted PI data frame
    ppp_arr = pd.DataFrame({"Number of points": num_point_arr, "Profit Per Point": ppp_arr})  # predicted PI data frame
    fig,ax = plt.subplots(2)
    pp_df[["Number of points", "Predicted PI"]].plot(x='Number of points', linestyle='-', marker='o',ax = ax[0])
    ppp_arr[["Number of points", "Profit Per Point"]].plot(x='Number of points', kind='bar', ax = ax[1])
    for i, j in pp_df["Predicted PI"].items():
        ax[0].annotate(str(round(j,4)), xy=(i, j))
    plt.show()
