def alpha_beta(depth, index, is_max, values, alpha, beta):
    if depth == 3:
        return values[index]
    if is_max:
        max_eval = -float('inf')
        for i in range(2):
            eval = alpha_beta(depth + 1, index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alpha_beta(depth + 1, index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
values = [3, 5, 6, 9, 1, 2, 0, -1]
optimal_value = alpha_beta(0, 0, True, values, -float('inf'), float('inf'))
print("The optimal value is:", optimal_value)
