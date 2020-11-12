#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyotrs import Article, Client, DynamicField, Ticket

title = sys.argv[1]
body  = sys.argv[2]

client = Client("https://URL", "USER", "PASSWORD")
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


print "SET VARIABLE \"RETURN\" \"$create_ticket\"\n";
