# BIT2118-Scientific-Computing
BIT 2118 – Scientific Computing: Group Work (Tasks 2–20)

 Brillian Andalo  
Reg. No.: BSCCS/2025/41447  
GitHub: [syder-a11y](https://github.com/syder-a11y)

This is my individual repository for the BIT 2118 Scientific Computing group work. For every task it contains:

1. the **base program** from the assignment (`code/`), run and checked;
2. the **same program with parameters changed** (`code/modified/`), showing how the result changes;
3. a **similar program for a different real-world case** (`code/realworld/`);
4. a **write-up** (`docs/`) that identifies the inputs and the mathematical operation, explains the output and graph, explains what changed when a parameter was changed, and documents the new case (assumptions, input data, output, interpretation);
5. the **saved console output** (`outputs/`) and **graphs** (`figures/`) from running the code.

## How to run

```bash
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py            # run one task
python code/modified/Task_02_numpy_arrays_modified.py      # parameters changed
python code/realworld/Task_02_numpy_arrays_realworld.py    # real-world case
./run_all.sh                                   # run everything and refresh outputs/ and figures/
```

Tested with Python 3.13, NumPy 2.5, SciPy 1.18, Matplotlib 3.11. (`np.trapezoid` in Task 16 needs NumPy 2.0 or newer; on older NumPy use `np.trapz`.)
Scripts that plot call `plt.show()`; `run_all.sh` sets a non-interactive backend so nothing pops up and the figures are only saved.

## Index

| Task | Topic | Original | Params changed | Real-world | Write-up | Graph(s) |
|---|---|---|---|---|---|---|
| A (Task 2) | NumPy arrays | [code](code/Task_02_numpy_arrays.py) | [code](code/modified/Task_02_numpy_arrays_modified.py) | [code](code/realworld/Task_02_numpy_arrays_realworld.py) | [doc](docs/Task_02_numpy_arrays.md) | – |
| B (Task 3) | Vectorization | [code](code/Task_03_vectorization.py) | [code](code/modified/Task_03_vectorization_modified.py) | [code](code/realworld/Task_03_vectorization_realworld.py) | [doc](docs/Task_03_vectorization.md) | – |
| C (Task 4) | Floating-point errors | [code](code/Task_04_numerical_errors.py) | [code](code/modified/Task_04_numerical_errors_modified.py) | [code](code/realworld/Task_04_numerical_errors_realworld.py) | [doc](docs/Task_04_numerical_errors.md) | – |
| D (Task 5) | Matrix algebra | [code](code/Task_05_matrix_algebra.py) | [code](code/modified/Task_05_matrix_algebra_modified.py) | [code](code/realworld/Task_05_matrix_algebra_realworld.py) | [doc](docs/Task_05_matrix_algebra.md) | [robot](figures/Task_05_modified_robot.png) |
| E (Task 6) | Linear systems | [code](code/Task_06_linear_systems.py) | [code](code/modified/Task_06_linear_systems_modified.py) | [code](code/realworld/Task_06_linear_systems_realworld.py) | [doc](docs/Task_06_linear_systems.md) | – |
| F (Task 7) | Gaussian elimination / LU | [code](code/Task_07_gaussian_lu.py) | [code](code/modified/Task_07_gaussian_lu_modified.py) | [code](code/realworld/Task_07_gaussian_lu_realworld.py) | [doc](docs/Task_07_gaussian_lu.md) | – |
| G (Task 8) | Iterative methods | [code](code/Task_08_iterative_linear.py) | [code](code/modified/Task_08_iterative_linear_modified.py) | [code](code/realworld/Task_08_iterative_linear_realworld.py) | [doc](docs/Task_08_iterative_linear.md) | [convergence](figures/Task_08_convergence.png), [plate](figures/Task_08_modified_plate.png) |
| H (Task 9) | Eigenvalues / eigenvectors | [code](code/Task_09_eigenvalues.py) | [code](code/modified/Task_09_eigenvalues_modified.py) | [code](code/realworld/Task_09_eigenvalues_realworld.py) | [doc](docs/Task_09_eigenvalues.md) | – |
| I (Task 10) | Bisection & fixed point | [code](code/Task_10_bisection_fixed_point.py) | [code](code/modified/Task_10_bisection_fixed_point_modified.py) | [code](code/realworld/Task_10_bisection_fixed_point_realworld.py) | [doc](docs/Task_10_bisection_fixed_point.md) | [equilibrium](figures/Task_10_equilibrium.png), [break-even](figures/Task_10_modified_breakeven.png) |
| J (Task 11) | Newton & secant | [code](code/Task_11_newton_secant.py) | [code](code/modified/Task_11_newton_secant_modified.py) | [code](code/realworld/Task_11_newton_secant_realworld.py) | [doc](docs/Task_11_newton_secant.md) | – |
| K (Task 12) | Nonlinear equations | [code](code/Task_12_nonlinear_equations.py) | [code](code/modified/Task_12_nonlinear_equations_modified.py) | [code](code/realworld/Task_12_nonlinear_equations_realworld.py) | [doc](docs/Task_12_nonlinear_equations.md) | – |
| L (Task 13) | Interpolation | [code](code/Task_13_interpolation.py) | [code](code/modified/Task_13_interpolation_modified.py) | [code](code/realworld/Task_13_interpolation_realworld.py) | [doc](docs/Task_13_interpolation.md) | [temperature](figures/Task_13_interpolation.png), [river](figures/Task_13_modified_river.png) |
| M (Task 14) | Curve fitting | [code](code/Task_14_curve_fitting.py) | [code](code/modified/Task_14_curve_fitting_modified.py) | [code](code/realworld/Task_14_curve_fitting_realworld.py) | [doc](docs/Task_14_curve_fitting.md) | [fit](figures/Task_14_curve_fit.png), [logistic](figures/Task_14_modified_logistic.png) |
| N (Task 15) | Numerical differentiation | [code](code/Task_15_numerical_differentiation.py) | [code](code/modified/Task_15_numerical_differentiation_modified.py) | [code](code/realworld/Task_15_numerical_differentiation_realworld.py) | [doc](docs/Task_15_numerical_differentiation.md) | [speed](figures/Task_15_speed.png), [step size](figures/Task_15_modified_step_size.png), [motorbike](figures/Task_15_modified_motorbike.png) |
| O (Task 16) | Numerical integration | [code](code/Task_16_numerical_integration.py) | [code](code/modified/Task_16_numerical_integration_modified.py) | [code](code/realworld/Task_16_numerical_integration_realworld.py) | [doc](docs/Task_16_numerical_integration.md) | – |
| P (Task 17) | Euler method | [code](code/Task_17_euler_ode.py) | [code](code/modified/Task_17_euler_ode_modified.py) | [code](code/realworld/Task_17_euler_ode_realworld.py) | [doc](docs/Task_17_euler_ode.md) | [cooling](figures/Task_17_euler_cooling.png), [error vs h](figures/Task_17_modified_error_vs_h.png), [fish pond](figures/Task_17_modified_fish_pond.png) |
| Q (Task 18) | ODEs with SciPy | [code](code/Task_18_scipy_ode.py) | [code](code/modified/Task_18_scipy_ode_modified.py) | [code](code/realworld/Task_18_scipy_ode_realworld.py) | [doc](docs/Task_18_scipy_ode.md) | [RC circuit](figures/Task_18_rc_circuit.png), [SIR](figures/Task_18_modified_sir.png) |
| R (Task 19) | Optimization | [code](code/Task_19_optimization.py) | [code](code/modified/Task_19_optimization_modified.py) | [code](code/realworld/Task_19_optimization_realworld.py) | [doc](docs/Task_19_optimization.md) | – |
| S (Task 20) | Monte Carlo | [code](code/Task_20_monte_carlo.py) | [code](code/modified/Task_20_monte_carlo_modified.py) | [code](code/realworld/Task_20_monte_carlo_realworld.py) | [doc](docs/Task_20_monte_carlo.md) | [overload risk](figures/Task_20_monte_carlo.png), [project](figures/Task_20_modified_project.png) |

Task 1 (Data Science Essentials with Python) is the self-paced prerequisite and has no code here.

 Notes
- The numbers in the write-ups come from the saved files in `outputs/`. Timing results (Task 3, Task 7) will differ on another computer; the speed-up ratios should be similar.
- Data in the modified cases (greenhouse, tariff, economy coefficients, app users, bakery, etc.) are **illustrative values chosen for the exercise**, not real measurements, and the fee tariff in Task 3 is not any operator's real tariff.
