#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t **tab, **tab2;
	int n = 1, i = 0;

	if (!list)
		return (0);
	tab = (listint_t **)malloc(sizeof(listint_t *) * n);
	tab[0] = list;
	list = list->next;
	while (list)
	{
		for (i = 0; i < n; i++)
		{
			if (list == tab[i])
				return (1);
		}
		n++;
		tab2 = (listint_t **)malloc(sizeof(listint_t *) * n);
		for (i = 0; i < n - 1; i++)
			tab2[i] = tab[i];
		tab2[i] = list;
		tab = tab2;
		list = list->next;
	}
	return (0);
}
