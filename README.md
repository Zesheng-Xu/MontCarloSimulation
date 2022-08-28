# MontCarloSimulation


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


How to use: 

  Adjust paramaters within main.py
  
  then
  
  ```python main.py```
