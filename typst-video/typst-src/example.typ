Hello Typst!
1. One
  1. two-dimensional
2. three
#figure(
image(
  "../figures/fig_temperature_distribution.png",
  width: 10cm, 
),
caption: [
  This is a caption
])

#line(length: 10cm, angle: -45deg)

#table(
  columns: 3,
  table.header([One],[One],[One]),
  [One],[One],[One],
  [One],[One],[One],
  [One],[One],[One],
  [One],[One],[One],
  [One],[One],[One],
  [One],[One],[One],

)


$A x = cal(b)$