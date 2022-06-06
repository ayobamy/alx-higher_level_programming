#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - a func that checks palindrome of singly linked list
 * @head: pointer to pointer to the first node of listint_t list
 *
 * Return: return 1, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	unsigned int len = 0, i = 0, flag = 1, lastidx, *buffer;

	current = *head;
	if (*head == NULL || head == NULL)
		return (1);

	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	buffer = malloc(sizeof(int) * len);
	if (buffer == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		buffer[i] = current->n;
		i++;
		current = current->next;
	}

	lastidx = len - 1;
	for (i = 0; i < len / 2; i++)
	{
		if (buffer[i] != buffer[lastidx - i])
		{
			flag = 0;
			break;
		}
	}
	free(buffer);
	return (flag);
}
