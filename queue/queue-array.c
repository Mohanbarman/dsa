#include <stdio.h>
#include <stdlib.h>

struct Queue {
  int size;
  int front;
  int rear;
  int *Q;
};

int enqueue(struct Queue *queue, int value) {
  if ((queue->rear + 1) % queue->size == queue->front) {
    printf("queue is full");
    return 0;
  }
  queue->rear = (queue->rear + 1) % queue->size;
  queue->Q[queue->rear] = value;
  return 1;
}

int dequeue(struct Queue *queue) {
  if (queue->front == queue->rear) {
    printf("queue is empty");
    return -1;
  }
  queue->front = (queue->front + 1) % queue->size;
  return queue->Q[queue->front];
}

void display_queue(struct Queue queue) {
  queue.front++;
  do {
    printf("%d ", queue.Q[queue.front]);
    queue.front = (queue.front + 1) % queue.size;
  } while ((queue.front) != (queue.rear + 1) % queue.size);
  printf("\n");
}

void create(struct Queue *queue, int size) {}

int main() {
  struct Queue queue;
  queue.size = 5;
  queue.front = 0;
  queue.rear = 0;
  queue.Q = malloc(sizeof(int) * queue.size);

  enqueue(&queue, 1);
  enqueue(&queue, 2);
  enqueue(&queue, 4);
  enqueue(&queue, 4);
  dequeue(&queue);
  enqueue(&queue, 5);

  display_queue(queue);

  return 0;
}
