import random

class MultiArmBanditOptimizer:
    def __init__(self):
        self.subject_lines = {
            "A": {"sends": 100, "opens": 20}, # 20%
            "B": {"sends": 100, "opens": 45}  # 45%
        }

    def select_optimal_subject(self):
        # Epsilon-greedy selection
        if random.random() < 0.1:
            choice = random.choice(list(self.subject_lines.keys()))
            print(f"[Lead Gen] Exploring random subject line: Variant {choice}")
            return choice
            
        best_variant = max(self.subject_lines, key=lambda k: self.subject_lines[k]["opens"] / self.subject_lines[k]["sends"])
        print(f"[Lead Gen] Exploiting winning subject line: Variant {best_variant}")
        return best_variant

if __name__ == "__main__":
    optimizer = MultiArmBanditOptimizer()
    optimizer.select_optimal_subject()
