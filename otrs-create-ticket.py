#!/usr/bin/env python3

import sys
from pyotrs import Article, Client, DynamicField, Ticket

title = "title"
body  = "body"


client = Client(URL, USER, PASSWORD)
client.session_create()

new_ticket = Ticket.create_basic(
                                Title=title,
                                Queue="Novos tickets via telefone",
                                State=u"new",
                                Priority=u"Media prioridade",
                                CustomerUser="pbx@qosit.com.br"
                                )

first_article = Article({"Subject": title, "Body": body})

create_ticket = client.ticket_create(new_ticket, first_article)

print(create_ticket, "Retorno função")
print(create_ticket['TicketNumber'])
print(type(create_ticket['TicketNumber']))
ticketnumber = create_ticket['TicketNumber']


variable = '"OTRSTICKET"'
aspas = '"'
variableValue = aspas + ticketnumber + aspas

print(variable)
if (ticketnumber == " "):
   print("set variable \"RETURN\" \"Ticket não criado, entre em contato com nosso time de suporte!\"")
else:
   print("set variable \"RETURN\" \"Seu ticket é:\"")
   print("set variable", variable, variableValue)
