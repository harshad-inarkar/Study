def h_index(citations: list[int]) -> int:
    """
    Calculate the h-index of a researcher.
    The h-index is the maximum value of h such that the researcher has published h papers
    that have each been cited at least h times.
    
    Parameters:
        citations: List[int] - Array of citation counts for each paper
    Returns:
        int - The h-index value
    """
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i
    
    return len(citations)

# Example usage
if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    result = h_index(citations)
    print(f"H-index: {result}")  # Output: 3
