# Плохие комментарии
BAD = 'COMMENT SHOULD BE DELETED'

for i in range(int(input())):
    comment = input()
    if not comment or comment.isspace():
        print(f'{i + 1}: {BAD}')
        continue
    print(f'{i + 1}: {comment}')
