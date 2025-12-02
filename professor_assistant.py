import random
import os

def load_question_bank(file_path):
    """
    Reads the file and organizes lines into Question and Answer pairs.
    """
    questions = []
    answers = []
    
    try:
        with open(file_path, 'r') as file:
           
            lines = [line.strip() for line in file.readlines() if line.strip()]
            
           
            for i in range(0, len(lines), 2):
                if i + 1 < len(lines):
                    questions.append(lines[i])
                    answers.append(lines[i+1])
                    
        return questions, answers, True
    except FileNotFoundError:
        return [], [], False

def main():
    print("Welcome to professor assistant version 1.0.")
    name = input("Please Enter Your Name: ")
    print(f"Hello Professor. {name}, I am here to help you create exams from a question bank.")

    while True:
       
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ")
        
        if choice.lower() == 'no':
            print(f"Thank you professor {name}. Have a good day!")
            break
        elif choice.lower() == 'yes':
           
            path = input("Please Enter the Path to the Question Bank. ")
            
           
            questions, answers, success = load_question_bank(path)
            
            if success and len(questions) > 0:
                print("Yes, indeed the path you provided includes questions and answers.")
                
               
                try:
                    num_needed = int(input("How many question-answer pairs do you want to include in your exam? "))
                except ValueError:
                    print("Invalid number. Please enter a valid integer.")
                    continue

              
                if num_needed > len(questions):
                    print(f"Note: The bank only has {len(questions)} questions. Selecting all of them.")
                    num_needed = len(questions)

               
                output_file = input("Where do you want to save your exam? ")

                
                selected_indices = []
                while len(selected_indices) < num_needed:
                   
                    rand_idx = random.randint(0, len(questions) - 1)
                    
                   
                    if rand_idx not in selected_indices:
                        selected_indices.append(rand_idx)
                
                
                try:
                    with open(output_file, 'w') as out_f:
                        for idx in selected_indices:
                            out_f.write(f"Q: {questions[idx]}\n")
                            out_f.write(f"A: {answers[idx]}\n\n")
                    
                    print(f"Congratulations Professor {name}. Your exam is created and saved in {output_file}.")
                except Exception as e:
                    print(f"An error occurred while saving the file: {e}")

            else:
                print("Error: Could not read the file or the file is empty. Please check the path.")
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")

if __name__ == "__main__":
    main()