def dice_similarity_coefficient(inter, union):
    return 2 * sum(inter) / (sum(union) + sum(inter))
