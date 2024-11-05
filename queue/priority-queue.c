#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node *next;
};

struct Queue {
  struct Node *front;
  struct Node *rear;
};

struct PriorityQ {
  struct Queue *p1;
  struct Queue *p2;
  struct Queue *p3;
  struct Queue *p4;
};

enum Priority {
  LOW,
  MEDIUM,
  HIGH,
  HIGHEST,
};

struct Queue *getQueueByPriority(struct PriorityQ *q, enum Priority priority) {
  struct Queue *queue = NULL;
  switch (priority) {
  case LOW:
    queue = q->p1;
  case MEDIUM:
    queue = q->p2;
  case HIGH:
    queue = q->p3;
  case HIGHEST:
    queue = q->p4;
  }
  return queue;
};

void enqueue(struct PriorityQ *q, enum Priority priority, int data) {
  struct Node *node = malloc(sizeof(struct Node));
  if (node == NULL) {
    printf("queue is full\n");
    return;
  }
  node->data = data;
  node->next = NULL;

  struct Queue *queue = getQueueByPriority(q, priority);

  if (queue == NULL) {
    printf("invalid priority");
    return;
  }

  if (queue->front == NULL) {
    queue->front = node;
    queue->rear = node;
  } else {
    queue->rear->next = node;
    queue->rear = node;
  }
}

int dequeue(struct PriorityQ *priorityQ) {
  int val = -1;
  if (q->front->next == NULL) {
    printf("queue is empty\n");
  } else {
    val = q->front->data;
    struct Node *temp_front = q->front->next;
    free(q->front);
    q->front = temp_front;
  }
  return val;
}

void Display(struct Queue *q) {
  struct Node *front = q->front;
  while (front != NULL) {
    printf("%d ", front->data);
    front = front->next;
  }
}

int main() { return 0; }
