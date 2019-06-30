import imaplib , email
uname='2017pcecsnimish106'
passwd='mittalnimish'
imap_url='imap.poornima.org'
def get_body(msg):
    if msg.is_multipart():
            return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)


con = imaplib.IMAP4_SSL(imap_url)
con.login(uname,passwd)

con.select('INBOX')
result, data = con.fetch(b'3','RFC822')
rav = email.message_from_bytes(data[0][1])
print(get_body(rav))

