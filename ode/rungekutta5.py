def rungekutta5(x1, x2, y0, h):
  """
  Runge-Kutta 5th (higher order) method to solve ODE at domain x [x1,x2] 
  
  x1: the lowest x in domain
  x2: the upper x in domain
  y0: y at initial condition (x0 = 0)
  h: stepsize
  """

  # initial condition
  y = y0

  # time array from timesteps
  x = np.arange(x1, x2+h, h)

  # parameters
  a = 0.5
  b = 0.5
  alpha = 1
  beta = 1

  x_rk5 = []
  y_rk5 = []

  for i in x:
    x_rk5.append(float(i))
    y_rk5.append(float(y))

    f1 = dfdx(i, y)
    k1 = h * f1

    f2 = dfdx((i + 0.25 * h), (y + 0.25 * k1))
    k2 = h * f2

    f3 = dfdx((i + 0.25 * h), (y + (1/8 * k1) + (1/8 * k2)))
    k3 = h * f3

    f4 = dfdx((i + 0.5 * h), (y - (0.5 * k2) + k3))
    k4 = h * f4

    f5 = dfdx((i + 0.75 * h), (y + (3/16 * k1) + (9/16 * k4)))
    k5 = h * f5

    f6 = dfdx((i + h), (y - (3/7 * k1) + (2/7 * k2) + (12/7 * k3) - (12/7 * k4) + (8/7 * k5)))
    k6 = h * f6
    
    y = y + ((1/90) * ((7 * k1) + (32 * k3) + (12 * k4) + (32 * k5) + (7 * k6)))

  return(x_rk5, y_rk5)
