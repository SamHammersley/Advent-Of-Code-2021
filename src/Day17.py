input = 'target area: x=209..238, y=-86..-59'[13:].split(', ')
input1 = 'target area: x=119..176, y=-141..-84'[13:].split(', ')
sample = 'target area: x=20..30, y=-10..-5'[13:].split(', ')

def enters_target_area(t_x1, t_y1, t_x2, t_y2, iv_x, iv_y):
  dx,dy = iv_x, iv_y
  x,y = (0,0)
  max_y = 0

  while not ((x > t_x2) or (y < t_y1) or (x < t_x1 and dx == 0)):
    x += dx
    y += dy
    max_y = max(y, max_y)
    if dx > 0: dx -= 1
    if dx < 0: dx += 1
    dy -= 1

    if t_x1 <= x <= t_x2 and t_y1 <= y <= t_y2:
      return max_y

def force(input):
  t_x1,t_x2 = map(int, input[0][2:].split('..'))
  t_y1,t_y2 = map(int, input[1][2:].split('..'))
  max_y = 0
  solutions = 0

  for vx in range(t_x2+1):
    for vy in range(t_y1, abs(t_y1)):
      y = enters_target_area(t_x1, t_y1, t_x2, t_y2, vx, vy)
      if y != None:
        max_y = max(y, max_y)
        solutions += 1

  return (max_y, solutions)

# better part 1 solution explanation:

#   Because the dY changes at a constant rate (-1 per step) and the starting position is 
#   fixed at (0,0), the higher the initial y velocity, the higher the trajectory curve reaches.

#   When the curve passes back through y=0, dY (change in y dir) is the initial y velocity * -1.
#   To demonstrate this, let us observe the change in y as we simulate trajectory in the following example
#   (the x component is irrelevant) starting with initial velocity 3:
#     yvelocity:       3      2      1      0     -1     -2     -3
#     positions: (0,0), (0,3), (0,5), (0,6), (0,6), (0,5), (0,3), (0,0)

#   Since at y=0 (on the way down after the peak), dY is -1 * initial y velocity the next dY value would be
#   -1 * initial y velocty - 1 and we know that the higher the initial velocity the higher the curve goes,
#   we need to maximise the initial y velocity.

#   The largest initial y velocity (such that the curve enters the target area on some step) is bound by the
#   minimum y value of the target area (the bottom of the target area). If the initial y velocity was any larger,
#   the next y position after y=0 would be below the bounds of the target area and therefore would not satisify 
#   the conditions for the problem.

#   So for the highest curve, -1 * initial y velocity - 1 must be equal to the target area's minimum y.
#   -1 * initial y velocity - 1 = target min x
#   initial y velocity = -(target min x + 1)
#   Now we know the largest possible initial y velocity is -(target min x + 1) we can use that to calculate how
#   high the trajectory curve will go. To calculate the height of the curve, we have to recognise that since the
#   dY value is decremented every step, the height of the curve is just the sum of natural numbers up to the initial velocity.

#   In the example above (to demonstrate the dY value at y=0, after the peak), we can see that the height is 6
#   or sum_of_natural_numbers(3) since the initial velocity is 3.

#   the solution to part 1, therefore, is sum_of_natural_numbers(-(target min x + 1))

def part1(input):
  t_y1,t_y2 = map(int, input[1][2:].split('..'))
  return t_y1*(t_y1 + 1) / 2

print(part1(input))
print(part1(sample))
print(force(sample))
print(force(input))
print(force(input1))
