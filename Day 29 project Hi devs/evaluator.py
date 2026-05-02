import math


class RecommendationEvaluator:

    @staticmethod
    def precision_at_k(recommendations, relevant_items, k):
        top_k = recommendations[:k]

        if not top_k:
            return 0.0

        relevant_found = len(set(top_k).intersection(set(relevant_items)))
        return round(relevant_found / k, 4)

    @staticmethod
    def recall_at_k(recommendations, relevant_items, k):
        if not relevant_items:
            return 0.0

        top_k = recommendations[:k]
        relevant_found = len(set(top_k).intersection(set(relevant_items)))

        return round(relevant_found / len(relevant_items), 4)

    @staticmethod
    def ndcg_at_k(recommendations, relevant_items, k):
        top_k = recommendations[:k]

        dcg = 0
        for i, item in enumerate(top_k):
            if item in relevant_items:
                dcg += 1 / math.log2(i + 2)

        ideal_dcg = sum(
            1 / math.log2(i + 2)
            for i in range(min(len(relevant_items), k))
        )

        if ideal_dcg == 0:
            return 0.0

        return round(dcg / ideal_dcg, 4)

    def evaluate_all(self, recommendations_dict, ground_truth_dict, k=5):
        precision_scores = []
        recall_scores = []
        ndcg_scores = []

        for user_id, recs in recommendations_dict.items():
            relevant = ground_truth_dict.get(user_id, [])

            precision_scores.append(
                self.precision_at_k(recs, relevant, k)
            )

            recall_scores.append(
                self.recall_at_k(recs, relevant, k)
            )

            ndcg_scores.append(
                self.ndcg_at_k(recs, relevant, k)
            )

        return {
            "avg_precision": round(sum(precision_scores) / len(precision_scores), 4),
            "avg_recall": round(sum(recall_scores) / len(recall_scores), 4),
            "avg_ndcg": round(sum(ndcg_scores) / len(ndcg_scores), 4)
        }