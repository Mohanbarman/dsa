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

void enqueue(struct Queue *q, int data) {
  struct Node *node = malloc(sizeof(struct Node));
  if (node == NULL) {
    printf("queue is full\n");
    return;
  }
  node->data = data;
  node->next = NULL;
  if (q->front == NULL) {
    q->rear = node;
    q->front = node;
  } else {
    q->rear->next = node;
    q->rear = node;
  }
}

int dequeue(struct Queue *q) {
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

int main() {
  struct Queue *q = malloc(sizeof(struct Queue));

  enqueue(q, 1);
  enqueue(q, 2);
  enqueue(q, 3);
  enqueue(q, 4);
  dequeue(q);
  Display(q);

  return 0;
}
