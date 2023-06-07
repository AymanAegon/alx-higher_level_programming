#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number){
	listint_t *new;
	listint_t *current, *prev;

	current = *head;
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	prev = current;
	current = current->next;
	while (current && current->n <= number)
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	prev->next = new;
	return (new);
}
