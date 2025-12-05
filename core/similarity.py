import numpy as np
from numpy.typing import NDArray

def cosine_similarity(a: list[float], b: list[float]) -> float:
    """
    Calculates the cosine similarity between two vectors.
    
    Args:
        a: First vector.
        b: Second vector.
        
    Returns:
        The cosine similarity score between -1.0 and 1.0.
    """
    vec_a: NDArray[np.float64] = np.array(a, dtype=np.float64)
    vec_b: NDArray[np.float64] = np.array(b, dtype=np.float64)
    
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
        
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))
