"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.
    """
    rounded = [round(score) for score in student_scores]
    return rounded


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.
    """

    best_list = []
    for score in student_scores:
        if score >= threshold:
            best_list.append(score)
    return best_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.
    """
    lower_threshold = [41]
    Value = (highest - 40)//4
    for i in range(3):
        lower = lower_threshold[i] + Value
        lower_threshold.append(lower)
    return lower_threshold


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.
    """

    ranking = []
    for i in range(1, len(student_names)+1):
        student_info = str(i) + '. ' + student_names[i-1] + ': ' + str(student_scores[i-1])
        ranking.append(student_info)
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.
    """
    perfect = []
    for i in range(len(student_info)):
        if student_info[i][1] == 100:
            return student_info[i]
            break
    return perfect

