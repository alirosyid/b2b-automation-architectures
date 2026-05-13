class FeatureFlagManager:
    """
    Enables Dark Launching and Canary Deployments for new AI features.
    Allows the agency to toggle new extraction logic or LLM models for specific 
    B2B clients without requiring a full system redeployment.
    """
    FLAGS = {
        "use_experimental_graph_rag": {"enabled": False, "rollout_percentage": 0},
        "route_to_gemini_2_5": {"enabled": True, "rollout_percentage": 100}
    }

    @classmethod
    def is_enabled(cls, feature_name: str, client_id: str = None) -> bool:
        flag = cls.FLAGS.get(feature_name)
        if not flag:
            return False
        # Future implementation: deterministic hashing based on client_id for partial rollouts
        return flag.get("enabled", False)
