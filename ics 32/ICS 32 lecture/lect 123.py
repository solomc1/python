#Yackety Protocol
#
# ONe main rule: Every message is a single line of text terminated with 'r/n'
# * Client initiates a connetino to the server
# * server accepts the connection
# * client sends
# * client sends the message "YACKETY_HELLO @alex"
# * Server responds either with the message
# *                 "YACKETY_HELLO" or "YACKETY_INVALID_USERNAME"
# * At this point, client can issue any of a few commands and server
# wil respond appropriately

#Commands

#*Yackety_Send any text you'd like to send
#   Sends a Yackety message to the server
#   Server responds with "Yackety_Sent"
# * YACKET _LAST #
#   Retrieves the last # messages that have been sent
#   Server responds with "YACKETY_MESS_COUNT #"
#       followed by YACKETY_MESSAGE @username text of the message"
# *     Server responds with "YACKETY_GOODBYE" and then closes the connection
