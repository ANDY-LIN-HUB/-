import numpy as np

def find_machine_zero(dtype):
    E_k = dtype(1.0)  # начальное знач.
    k = 0  # каунтер

    while E_k > 0:
        E_k_next = E_k / 2
        if E_k_next == 0:
            break
        E_k = E_k_next
        k += 1

    return E_k, k


result_f32 = find_machine_zero(np.float32)
result_f64 = find_machine_zero(np.float64)

print("1.1 Положительная граница машинного нуля:")
print(f"Для float32: E_k = {result_f32[0]}, итерации: {result_f32[1]}")
print(f"Для float64: E_k = {result_f64[0]}, итерации: {result_f64[1]}")


def find_machine_epsilon(dtype):
    E_k = dtype(1.0)  
    k = 0  # 

    while True:
        F_k = dtype(1.0) + E_k / 2  
        if F_k == dtype(1.0): 
            break
        E_k /= 2 
        k += 1

    return E_k, k


epsilon_float32 = find_machine_epsilon(np.float32)
epsilon_float64 = find_machine_epsilon(np.float64)

print("\n1.2 Машинное эпсилон:")
print(f"Для float32: E_k = {epsilon_float32[0]}, итерации: {epsilon_float32[1]}")
print(f"Для float64: E_k = {epsilon_float64[0]}, итерации: {epsilon_float64[1]}")

