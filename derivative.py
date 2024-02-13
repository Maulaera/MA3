import math
# import matplotlib.pyplot as plt

def f(x):
    return math.sin(x)

def f_prime(x):
    return math.cos(x)

def finite_difference(x,h):
    return (f(x+h)-f(x)) / h

def known_derivative(x):
    return f_prime(x)

def absolute_error(approx_value, known_value):
    return abs(approx_value - known_value)

def cleve_moler_eps():
    eps = 1.0
    for _ in range(1000):
        if 1.0 + eps == 1.0:
            break
        eps /= 2.0
    return eps

def main():
    x = 1
    h_values = [2 ** -i for i in range(1,31)]

    print("|  h  |    x    | Approx. f'(x) |  Known f'(x)  |  Abs. Error  |")
    print("|:---:|:-------:|:-------------:|:-------------:|:------------:|")

    for h in h_values:
        approx_derivative = finite_difference(x,h)
        known_value = known_derivative(x)
        abs_error = absolute_error(approx_derivative, known_value)
        print(f"|{h:<6.5f}|{x:^15.8f}|{approx_derivative:^15.8f}|{known_value:^15.8f}|{abs_error:^15.8f}")

    eps = cleve_moler_eps()
    sqrt_eps = math.sqrt(eps)
    print(f"\nApproximated eps using Cleve Moler Algorithm: {eps}")
    print(f"Square root of eps: {sqrt_eps}")


    # Plotting 
   # plt.figure(figsize=(10,6))
   # plt.plot(h_values, abs_error, marker='o', color='blue',linestyle='')
   # plt.xscale('log')
   # plt.yscale('log')
   # plt.title('Absolute Error vs. Step Size (h)')
   # plt.xlabel('Step Size (h)')
   # plt.ylabel('Absolute Error')
   # plt.grid(True, which="both",ls="--",lw=0.5)
   # plt.tight_layout()
   # plt.savefig('absolute_error_vs_step_size.png')
   # plt.show()

    # print("\nApproximated eps using Cleve Moler Algorithm:", eps)
    # print("Square root of eps:", sqrt_eps)
    

if __name__ == "__main__":
    main()