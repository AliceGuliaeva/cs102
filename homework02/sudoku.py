from typing import Tuple, List, Set, Optional


def read_sudoku(filename: str) -> List[List[str]]:
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(str(grid[row][col]).center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


from typing import Tuple, List, Set, Optional
def group(values: List[str], n: int) -> List[List[str]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    d=n
    c=[]
    j=0
    for i in range(n):
        c.append([values[d] for d in range(j,d)])
        j=j+n
        d=d+n
    return(c)
    pass


def get_row(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    c=[a for a in grid[pos[0]]]
    return(c)
    pass


def get_col(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    c=[grid[i][pos[1]] for i in range(len(grid))]
    return(c)
    pass


def get_block(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    c=[]
    for i in range((pos[0]//3*3),(pos[0]//3*3+3)):
        for j in range((pos[1]//3*3),(pos[1]//3*3+3)):
            c.append(grid[i][j])
    return(c)
    pass


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    k=0
    b=(10,10)
    for i in range(len(grid)):
        if k!=1:
            for j in range(len(grid)):
                if k!=1:
                    if grid[i][j]=='.':
                        b=(i,j)
                        return(b)
                        k=1
    if b==(10,10):
        return(b)
    pass

def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    """ Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    a=set(get_block(grid,pos)+get_col(grid,pos)+get_row(grid,pos))
    b=set()
    for i in a:
        if i!='.':
            b.add(int(i))
    c=set()
    
    for i in range(1,10):
        if i in b:
            b.remove(i)
        else:
            c.add(str(i))
    return(c)
    pass


def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    grid1=grid
    if (find_empty_positions(grid1))==(10,10):
        return(grid1)
    else:
        b=find_empty_positions(grid1)
        a=set(find_possible_values(grid1,b))
        for i in a:
            grid1[b[0]][b[1]]=i
            solve(grid1)
            if (find_empty_positions(grid1))==(10,10):
                return(grid1)
            else:
                grid1[b[0]][b[1]]='.'

    pass

def check_solution(solution: List[List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    b=True
    for i in range(9):
        a={"1","2","3","4","5","6","7","8","9"}
        if set(get_col(solution,(0,i)))!=a:
            b=False
        if set(get_row(solution,(i,0)))!=a:
            b=False
        for j in range(9):
            if set(get_block(solution,(i,j)))!=a:
                b=False
    return(b)
    pass


import random
def generate_sudoku(N: int) -> List[List[str]]:
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    c=[[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]
    
    for i in range(3):
        d=random.randint(0,2)
        e=random.randint(0,2)
        for j in range(9):
            t1=c[d][j]
            c[d][j]=c[e][j]
            c[e][j]=t1
        for j in range(9):
            t1=c[j][d]
            c[j][d]=c[j][e]
            c[j][e]=t1
        d=random.randint(3,5)
        e=random.randint(3,5)
        for j in range(9):
            t1=c[d][j]
            c[d][j]=c[e][j]
            c[e][j]=t1
        for j in range(9):
            t1=c[j][d]
            c[j][d]=c[j][e]
            c[j][e]=t1
        d=random.randint(6,8)
        e=random.randint(6,8)
        for j in range(9):
            t1=c[d][j]
            c[d][j]=c[e][j]
            c[e][j]=t1
        for j in range(9):
            t1=c[j][d]
            c[j][d]=c[j][e]
            c[j][e]=t1
    for k in range(81-N):
        i=random.randint(0,8)
        j=random.randint(0,8)
        while c[i][j]=='.':
            i=random.randint(0,8)
            j=random.randint(0,8)
        c[i][j]='.'
    return(c)
    pass


"""if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        grid1=grid
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)"""
"print(generate_sudoku(1))"


