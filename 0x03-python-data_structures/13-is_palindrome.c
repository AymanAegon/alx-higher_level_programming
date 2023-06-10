#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len = 0, i = 0, *arr;

	temp = *head;
	
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	temp = *head;
	arr = (int *)malloc(sizeof(int) * len / 2);
	for (i = 0; i < len / 2; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	if (len > 1 && len % 2 == 1)
		temp = temp->next;
	for (i = len / 2 - 1; i >= 0; i--)
	{
		if (arr[i] != temp->n)
			return 0;
		temp = temp->next;
	}
	free(arr);
	return 1;
}
