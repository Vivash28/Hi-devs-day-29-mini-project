class RecommendationScorer:

    def __init__(self):
        self.scorers = {}

    def add_scorer(self, name, function, weight):
        self.scorers[name] = {
            "function": function,
            "weight": weight
        }

    def calculate_score(self, user_id, item_id, context=None):
        total_score = 0
        total_weight = 0
        explanation = []

        for name, scorer in self.scorers.items():
            score = scorer["function"](user_id, item_id, context)
            weight = scorer["weight"]

            total_score += score * weight
            total_weight += weight

            explanation.append(f"{name}: {score}")

        if total_weight == 0:
            final_score = 0.0
        else:
            final_score = round(total_score / total_weight, 4)

        return {
            "item_id": item_id,
            "score": final_score,
            "reason": ", ".join(explanation)
        }

    def rank_candidates(self, user_id, candidates, limit=10):
        results = []

        for item in candidates:
            results.append(
                self.calculate_score(user_id, item)
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:limit]