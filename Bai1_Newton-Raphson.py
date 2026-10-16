import numpy as np


# f(x, y) = 2(x - 1)^2 + 2(x - 1)(y + 2) + 2(y + 2)^2
def f(u):
    x, y = u
    return (
        2 * (x - 1)**2
        + 2 * (x - 1) * (y + 2)
        + 2 * (y + 2)**2
    )


def grad(u):
    x, y = u
    return np.array([
        4 * (x - 1) + 2 * (y + 2),
        2 * (x - 1) + 4 * (y + 2)
    ])


def hessian(u):
    return np.array([
        [4, 2],
        [2, 4]
    ])


def newton_optim(u_0, grad_fn, hessian_fn, tol=1e-6, max_iter=100):
    u = u_0
    for _ in range(max_iter):
        g = grad_fn(u)
        if np.linalg.norm(g) < tol:
            break
        H = hessian_fn(u)
        t = np.linalg.solve(H, -g)
        u = u + t
    return u


if __name__ == "__main__":
    u_0 = np.array([0.0, 0.0])
    u_optim = newton_optim(u_0, grad, hessian)
    print("Diem cuc tri:", u_optim)
    print("Gia tri ham:", f(u_optim))