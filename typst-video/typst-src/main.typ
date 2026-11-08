#let input_data = json("../data/inputs.json")
#let output_data = json("../data/outputs.json")

#set par(
  justify: true,
  leading: 0.65em,
)

#set heading(numbering: "1.1")
#set math.equation(numbering: "(1)")

// --------------------------------------------------
// Publication header
// --------------------------------------------------

#align(center)[
  #text(size: 15pt, weight: "bold")[Younes Lab Reports]

  #text(size: 9pt, fill: gray)[TECHNICAL REPORT | COMPUTATIONAL ENGINEERING]


  #line(length: 100%, stroke: 0.8pt)


  #text(size: 21pt, weight: "bold")[
    Transient Heat Conduction in a 2D Plate
  ]

  #text(size: 11pt)[Younes A. Toumi]

  #text(size: 9pt, fill: gray)[
    Computational Engineering | Independent Research
  ]

  #text(size: 9pt)[#datetime.today().display("[day]-[month]-[year]")]
]


// --------------------------------------------------
// Abstract
// --------------------------------------------------
#line(
  length: 100%,
  stroke: luma(7.45%),
)

#block(
  fill: luma(245),
  inset: 12pt,
)[
  #text(weight: "bold", size: 12pt)[Abstract]

  This paper presents a numerical study of the transient heat conduction in a two-dimensional aluminum plate. The governing heat equation is discretized using an explicit finite-difference scheme and solved computationally in Python. The temperature field is examined at selected simulation times to illustrate the transient response under prescribed initial and boundary conditions.

  *Keywords:* Heat conduction, finite-difference method, numerical simulation, Python, YounesLab.
]
#line(
  length: 100%,
  stroke: luma(7.45%),
)

#show: columns(2)[

  // --------------------------------------------------
  // 1. Introduction
  // --------------------------------------------------

  = Introduction

  Heat transfer is a fundamental phenomenon in mechanical and thermal engineering. Numerical methods provide a practical means of predicting temperature distributions in systems where analytical solutions are difficult to obtain. This study investigates transient heat conduction in a two-dimensional  plate. The objectives are to solve the governing equation numerically, visualize the evolution of the temperature field, and demonstrate the integration of computational results into a reproducible scientific document.

  // --------------------------------------------------
  // 2. Mathematical model
  // --------------------------------------------------

  = Mathematical Model
  == Governing equation

  The transient temperature field in a homogeneous, isotropic solid without internal heat generation is governed by @eq:heat:

  $ frac(partial T, partial t) = alpha ( frac(partial^2 T, partial x^2) + frac(partial^2 T, partial y^2) ) $ <eq:heat>

  where $T$ denotes temperature in degrees celcius $[°C]$, and $alpha$ is the thermal diffusivity expressed as a surface per unit of time $["mm" ^2/s]$.

  == Initial and boundary conditions

  The plate is initially at a uniform temperature of #input_data.initial_temperature_C °C. Each edge can be definied with a specified temperature, the top, right, bottom, and left edge are fixed to #input_data.boundary_temperature_C.top, #input_data.boundary_temperature_C.right, #input_data.boundary_temperature_C.bottom, and #input_data.boundary_temperature_C.left °C respectively.
  
  The plate dimensions is definied by its length and height here $ #input_data.length_mm times #input_data.height_mm ["mm"^2]$, the thermal diffusivity $alpha=#input_data.diffusivity_mm2_s ["mm"^2/s]$, spatial discretization is considered space invariant $Delta x = Delta y = #input_data.space_step_mm ["mm"]$, and simulation duration for the numerical model is $ t_("sim") = #input_data.total_time_s [s]$.

  // --------------------------------------------------
  // 3. Numerical methodology
  // --------------------------------------------------

  = Numerical Methodology

  == Spatial and temporal discretization

  The governing equation is discretized using the explicit forward-time central-space (FTCS) finite-difference method. Spatial derivatives are approximated using second-order central differences, and time integration is performed explicitly. Author in @video-heat-equation explored this phenomenon extensively.

  == Stability criterion

  For a uniform grid, the explicit scheme satisfies the stability condition

  $ alpha Delta t ( frac(1, Delta x^2) + frac(1, Delta y^2) ) <= 1/2 $

  where $Delta t$ is the time step and $Delta x$ and $Delta y$ denote the spatial grid spacings.

  == Numerical implementation

  The solver is implemented in Python using NumPy for numerical computation and Matplotlib for visualization. The temperature field is updated iteratively, while simulation parameters and numerical outputs are exported for subsequent analysis and document generation.

  // --------------------------------------------------
  // 4. Results and discussion
  // --------------------------------------------------

  = Results and Discussion

  == Temperature field evolution

  The temperature field is examined at the initial, intermediate, and final simulation times. @fig:temperature compares the spatial distribution of temperature across these three states.

  #figure(
    image("../figures/fig_temperature_distribution.png", width: 100%),
    caption: [Temperature distribution at selected simulation times.],
  ) <fig:temperature>

  == Center temperature evolution

  The temperature at the geometric center is monitored to characterize the transient response of the plate.

  #figure(
    image("../figures/fig_temperature_evolution.png", width: 70%),
    caption: [Temperature evolution of the plate.],
  ) <fig:center>

== Discussion


#let mean-temp = calc.round(output_data.mean_temperature_C * 100) / 100
#let center-temp = calc.round(output_data.center_temperature_C * 100) / 100
#let temp-diff = calc.round(calc.abs(output_data.mean_temperature_C - output_data.center_temperature_C) * 100) / 100
#let sim-time = calc.round(output_data.simulation_time_s * 100) / 100

Heat diffuses from the heated boundaries toward the initially cooler interior. As time progresses, the temperature field approaches a uniform equilibrium state.

At the final simulation time the mean plate temperature reached $#mean-temp [°C]$, while the temperature at the plate center sat at $#center-temp [°C]$. Their absolute difference is only $#temp-diff [°C]$, indicating that the temperature field is nearly uniform.

The simulation required approximately $#sim-time [s]$ of computational time. This value characterizes the execution time for the present implementation and hardware, rather than the physical duration of the simulated process.

These results illustrate how numerical outputs can be imported directly into a scientific document and rounded consistently without manually copying values from Python.

  // --------------------------------------------------
  // 5. Conclusion
  // --------------------------------------------------

  = Conclusion

  A two-dimensional transient heat-conduction problem was solved using an explicit finite-difference scheme implemented in Python. The resulting temperature fields illustrate the evolution toward thermal equilibrium under prescribed boundary conditions.

  The workflow also demonstrates how simulation parameters, numerical results, and figures can be integrated into a scientific document without manual duplication, supporting reproducible computational engineering.

  // --------------------------------------------------
  // References
  // --------------------------------------------------

  #bibliography("../references/library.bib", style: "ieee")
]
