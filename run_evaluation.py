from evaluation import ChatbotEvaluator
from app import get_best_response

class SimpleChatbot:
    def __init__(self):
        self.threshold = 0.3  # Threshold untuk formal cases
    
    def get_response(self, message):
        result = get_best_response(message, self.threshold)
        return {
            'intent': result.get('matched_intent', 'unknown'),
            'confidence': result.get('confidence', 0),
            'response': result.get('response', '')
        }

def main():
    print("=== Starting Chatbot Evaluation ===")
    print("-" * 50)
    
    # Initialize evaluator
    evaluator = ChatbotEvaluator()
    
    # Print data statistics
    evaluator.print_statistics()
    
    # Initialize chatbot
    chatbot = SimpleChatbot()
    
    # Run evaluation
    results = evaluator.evaluate_accuracy(chatbot)
    
    # Print detailed results
    evaluator.print_detailed_results(results)

if __name__ == "__main__":
    main() 