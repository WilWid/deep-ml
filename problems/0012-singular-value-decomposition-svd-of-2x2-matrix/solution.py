import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    
    B = np.transpose(A) @ A
    theta = 0.5 * np.arctan2(2 * B[0][1], B[0][0] - B[1][1])
    V = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    C = A @ V
    
    sigma1 = np.sqrt(np.transpose(C[:,0]) @ C[:,0])
    sigma2 = np.sqrt(np.transpose(C[:,1]) @ C[:,1])

    U = np.array([1 / sigma1 * C[:,0], 1 / sigma2 * C[:,1]])
    Sigma = np.array([sigma1, sigma2])

    return (np.transpose(U),Sigma,np.transpose(V))
    