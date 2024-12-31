import string
def arithmetic_arranger(problems, show_answers=False):
    length_of_problems=len(problems)
    if length_of_problems>5:
        return 'Error: Too many problems.'
    problem_sentence=" ".join(problems).split(' ')
    list_with_integers=list()
    #begin by checking whether the inputs are valid according to the rules
    for char in problem_sentence:
        if char.isdigit():
            if len(char)<5:
                change_to_integer=int(char)
                list_with_integers.append(change_to_integer)
            else:
                return 'Error: Numbers cannot be more than four digits.'
        elif char in string.punctuation:
            if char not in ('-', '+'):
                return "Error: Operator must be '+' or '-'."
            else:
                list_with_integers.append(char)
        else:
            return 'Error: Numbers must only contain digits.'
    #after checking the input and is valid we can now execute
    space1=" "*4 #spaces between each problem

    i=0
    j=1
    k=2
    problem_list=[]
    row1_list=[]
    row2_list=[]
    dashes_list=[]
    ans_list=[]
    while k < len(list_with_integers):
        length_of_adjustment=(max(len(str(list_with_integers[i])), len(str(list_with_integers[k])))+2)
        row1=space1+(str(list_with_integers[i]).rjust(length_of_adjustment))
        row1_list.append(row1)
        row2=(space1+list_with_integers[j]+str(list_with_integers[k]).rjust(length_of_adjustment-1))
        row2_list.append(row2)
        dashes=space1+"-"*length_of_adjustment
        dashes_list.append(dashes)
        if list_with_integers[j]=='+':
            ans = list_with_integers[i] + list_with_integers[k]
            adjusted_ans =space1 + (str(ans).rjust(length_of_adjustment))
            ans_list.append(adjusted_ans)
        else:
            ans = list_with_integers[i] - list_with_integers[k]
            adjusted_ans=space1+(str(ans).rjust(length_of_adjustment))
            ans_list.append(adjusted_ans)
        formated_view=(row1+"\n"+row2+"\n"+dashes+"\n"+space1+(str(ans).rjust(length_of_adjustment)))
        i+=3
        j+=3
        k+=3
    row1_final=''.join(row1_list)
    row2_final=''.join(row2_list)
    dashes_final=''.join(dashes_list)
    ans_final=''.join(ans_list)
    if show_answers:
        problem = (row1_final[4:]+"\n" +row2_final[4:]+"\n" +dashes_final[4:] +"\n"+ans_final[4:])
        return problem
    else:
        problem = (row1_final[4:]+"\n"+row2_final[4:]+"\n"+dashes_final[4:])
        return problem

    #after fixing put the return in if show_answers=true

print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"])}')
