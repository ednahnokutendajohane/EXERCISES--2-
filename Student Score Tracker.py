import json
import os

FILE_NAME = "student_scores.json"

def load_scores():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return {}

def save_scores(scores):
    with open(FILE_NAME, 'w') as f:
        json.dump(scores, f, indent=4)

def add_student(scores):
    name = input("Enter studenzt name: ").strip()
    try:
        score = float(input(f"Enter {name}'s score: "))
        scores[name] = score
        print(f"Added {name} with score {score}")
    except ValueError:
        print("Invalid score. Please enter a number.")

def view_all_scores(scores):
    if not scores:
        print("No student records found.")
        return
    print("\n--- All Student Scores ---")
    for name, score in scores.items():
        print(f"{name}: {score}")
    print("")

def update_score(scores):
    name = input("Enter student name to update: ").strip()
    if name in scores:
        try:
            new_score = float(input(f"Enter new score for {name}: "))
            scores[name] = new_score
            print(f"Updated {name}'s score to {new_score}")
        except ValueError:
            print("Invalid score. Please enter a number.")
    else:
        print(f"{name} not found.")

def delete_score(scores):
    name = input("Enter student name to delete: ").strip()
    if name in scores:
        del scores[name]
        print(f"Deleted {name}'s record.")
    else:
        print(f"{name} not found.")

def calculate_statistics(scores):
    if not scores:
        print("No scores to calculate.")
        return
    
    score_list = list(scores.values())
    average = sum(score_list) / len(score_list)
    high_score = max(score_list)
    low_score = min(score_list)
    
    print("\n Statistics ")
    print(f"Average Score: {average:.2f}")
    print(f"High Score: {high_score}")
    print(f"Low Score: {low_score}")
    print(" ")

def main():
    scores = load_scores() # 7. Load records when program starts
    print("Student Score Tracker loaded. Welcome!")
    
    while True:
        print("\n1. Add student and their score")
        print("2. View all student scores")
        print("3. Update student's score")
        print("4. Delete student's score")
        print("5. Calculate statistics")
        print("6. Save & Exit")
        
        choice = input("Choose an option 1-6: ").strip()
        
        if choice == '1':
            add_student(scores)
        elif choice == '2':
            view_all_scores(scores)
        elif choice == '3':
            update_score(scores)
        elif choice == '4':
            delete_score(scores)
        elif choice == '5':
            calculate_statistics(scores)
        elif choice == '6':
            save_scores(scores) # 6. Save record to a file
            print("Records saved. Goodbye!")
            break
        else:
            print("Invalid option. Try 1-6.")

if __name__ == "__main__":
    main()