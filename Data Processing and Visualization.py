# Note- This is a sample file for data processing and visualization.
# All data are assumed to be valid and in the correct format.
# Data part is the assumptions. This project only for demonstration purposes.

# Note- I think, I clear all the doubts.

# Note- 'requests' library is used to fetch data from API.
# 'matplotlib' library is used for visualization student exam score.
import requests
import matplotlib.pyplot as plt

# Step 1: Fetch data from API (simulated here).
def fetch_scores():
    # Simulated API response.
    # In real case: response = requests.get("https://api.example.com/scores").json().
    # But now we are only have simulated data okay.
    data = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 90},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 92},
        {"name": "Eva", "score": 88}
    ]
    return data

# Step 2: Process data (calculate average) to assumptions the whole data.
def calculate_average(data):
    scores = [student["score"] for student in data]
    avg_score = sum(scores) / len(scores)
    return avg_score, scores

# Step 3: Visualization of students' scores.
def visualize_scores(data, avg_score):
    names = [student["name"] for student in data]
    scores = [student["score"] for student in data]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(names, scores, color="skyblue", edgecolor="black")

    # Add average line.
    plt.axhline(y=avg_score, color="red", linestyle="--", label=f"Average: {avg_score:.2f}")

    # Annotate each bar with students score.
    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 str(score), ha="center", va="bottom")

    plt.title("Students' Test Scores")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Step 4: Main think is here so run it.
if __name__ == "__main__":
    data = fetch_scores()
    avg_score, scores = calculate_average(data)
    print(f"Average Score: {avg_score:.2f}")
    visualize_scores(data, avg_score)
