class CandidateGenerator:

    def __init__(self):
        self.user_history = {
            1: [101, 102, 103],
            2: [102, 104, 105],
            3: [101, 105, 106],
            4: []
        }

        self.item_similarity = {
            101: [107, 108],
            102: [109],
            103: [110],
            104: [111],
            105: [112]
        }

        self.popular_items = [201, 202, 203, 204, 205]

    def collaborative_candidates(self, user_id):
        if user_id not in self.user_history:
            return self.popularity_candidates()

        user_items = set(self.user_history[user_id])
        candidates = set()

        for other_user, items in self.user_history.items():
            if other_user != user_id:
                if user_items.intersection(items):
                    candidates.update(items)

        candidates -= user_items
        return list(candidates)[:20]

    def content_based_candidates(self, user_id):
        if user_id not in self.user_history or not self.user_history[user_id]:
            return self.popularity_candidates()

        candidates = set()

        for item in self.user_history[user_id]:
            if item in self.item_similarity:
                candidates.update(self.item_similarity[item])

        return list(candidates)[:20]

    def popularity_candidates(self):
        return self.popular_items[:20]

    def hybrid_candidates(self, user_id):
        combined = set()

        combined.update(self.collaborative_candidates(user_id))
        combined.update(self.content_based_candidates(user_id))
        combined.update(self.popularity_candidates())

        return list(combined)[:30]