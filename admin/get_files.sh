assignmentHandle=$1
echo 'Getting info to grade' $assignmentHandle
mkdir grades/$assignmentHandle

for b in $(git branch -r | grep 'develop-'); do
    echo
    echo
    echo 'Accessing branch' $b
    git checkout $b
    git show | head -3
    cp assignments/submission$assignmentHandle.md grades/$assignmentHandle/${b##origin\/}.md
done;
