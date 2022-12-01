def part_one():
    highest_calories = -1

    with open('day_1_input.txt', 'r') as f:

        current_sum = 0
        while True:
            line = f.readline()

            if not line:
                break

            if line != '\n':
                current_sum += int(line)
            else:
                highest_calories = current_sum if current_sum > highest_calories else highest_calories
                current_sum = 0

    print(highest_calories)

def part_two():
    def add_to_queue(queue, calories):
        if len(queue) < 3:
            queue.append(calories)
            queue.sort(reverse=True)
            return queue

        position = -1
        for i in range(len(queue)):
            if calories > queue[i]:
                position = i
                break

        if position == -1:
            return queue

        if position == len(queue)-1:
            queue[len(queue)-1] = calories
        else:
            queue = queue[:position] + [calories] + queue[position:len(queue)-1]

        return queue

    highest_calories = []

    with open('day_1_input.txt', 'r') as f:

        current_sum = 0
        while True:
            line = f.readline()

            if not line:
                break

            if line != '\n':
                current_sum += int(line)
            else:
                highest_calories = add_to_queue(highest_calories, current_sum)
                current_sum = 0

    print(highest_calories)
    print(f'Sum = {sum(highest_calories)}')

if __name__ == "__main__":
    part_one()
    part_two()
