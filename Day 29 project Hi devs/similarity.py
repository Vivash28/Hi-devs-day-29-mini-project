import math

class SimilarityCalculator:

    @staticmethod
    def cosine_similarity(vec1, vec2):
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(b * b for b in vec2))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return round(dot_product / (magnitude1 * magnitude2), 4)

    @staticmethod
    def jaccard_similarity(set1, set2):
        if not set1 and not set2:
            return 1.0

        union = len(set1.union(set2))
        intersection = len(set1.intersection(set2))

        if union == 0:
            return 0.0

        return round(intersection / union, 4)

    @staticmethod
    def pearson_correlation(r1, r2):
        if not r1 or not r2 or len(r1) != len(r2):
            return 0.0

        n = len(r1)
        mean1 = sum(r1) / n
        mean2 = sum(r2) / n

        numerator = sum((a - mean1) * (b - mean2) for a, b in zip(r1, r2))

        denominator1 = math.sqrt(sum((a - mean1) ** 2 for a in r1))
        denominator2 = math.sqrt(sum((b - mean2) ** 2 for b in r2))

        if denominator1 == 0 or denominator2 == 0:
            return 0.0

        return round(numerator / (denominator1 * denominator2), 4)