"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    for score in student_scores:
        round(student_scores[score])
    return student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_list = []
    for score in student_scores:
        if score >= threshold:
            best_list.append(score)
    return best_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
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
        student_info = str(i) + '.' + student_names[i-1] + ': ' + str(student_scores[i-1])
        ranking.append(student_info)
    return ranking

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.
    """
    perfect = []
    for i in range(len(student_info)+1):
        if student_info[i][1] == 100:
            return student_info[i]
            break
    
        return perfect
print(perfect_score([['Jan', 45], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]]))