def minimax(node, depth, is_maximizing_player, alpha, beta):
    if isinstance(node, int):
        return node
    if is_maximizing_player:
        best_val = float('-inf')
        for child in node:
            val = minimax(child, depth + 1, False, alpha, beta)  
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break  
        return best_val
    else:
        best_val = float('inf')
        for child in node:
            val = minimax(child, depth + 1, True, alpha, beta) 
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                break 
        return best_val
tree = [
    [ 
        [3, 5], 
        [6, 9]     
    ],
    [ 
        [1, 2],  
        [0, -1]  
    ]
]
optimal_value = minimax(tree, 0, True, float('-inf'), float('inf'))
print(f"Optimal value: {optimal_value}")
