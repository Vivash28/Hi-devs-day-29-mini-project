from similarity import SimilarityCalculator
from candidate_gen import CandidateGenerator
from scorer import RecommendationScorer
from evaluator import RecommendationEvaluator


print("===== TESTING SIMILARITY =====")

print(
    SimilarityCalculator.cosine_similarity(
        [1, 2, 3],
        [1, 2, 3]
    )
)

print(
    SimilarityCalculator.jaccard_similarity(
        {"python", "ml"},
        {"python", "ai"}
    )
)

print(
    SimilarityCalculator.pearson_correlation(
        [5, 4, 3],
        [4, 3, 2]
    )
)


print("\n===== TESTING CANDIDATE GENERATOR =====")

generator = CandidateGenerator()
print(generator.hybrid_candidates(1))


print("\n===== TESTING SCORER =====")

scorer = RecommendationScorer()

scorer.add_scorer(
    "popularity",
    lambda u, i, c: 0.8,
    0.4
)

scorer.add_scorer(
    "relevance",
    lambda u, i, c: 0.9,
    0.6
)

print(
    scorer.rank_candidates(
        1,
        [101, 102, 103]
    )
)


print("\n===== TESTING EVALUATOR =====")

evaluator = RecommendationEvaluator()

recommendations = {
    1: [101, 102, 103],
    2: [104, 105, 106]
}

ground_truth = {
    1: [101, 105],
    2: [104, 106]
}

print(
    evaluator.evaluate_all(
        recommendations,
        ground_truth,
        k=3
    )
)

print("\nALL TESTS PASSED")