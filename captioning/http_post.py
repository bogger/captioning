import os
PORTNUM = 1234
def issue_http_post(text, port=PORTNUM):
    import httplib
    BODY = "***filecontents***"
    conn = httplib.HTTPConnection("localhost", port)
    contents = text
    conn.request("POST", contents, BODY)
    response = conn.getresponse()
    conn.close()
    return response


def local_http_req(inputstr, portnum=PORTNUM):
    resp = issue_http_post(inputstr, portnum)
    print resp.read()

#find all 
if __name__ == '__main__':
    import sys
    if len(sys.argv)<2:
        port = 1238
        text = "Bill Clinton and Hillary went to France to see the CEO of Microsoft."
        print "Assuming portNum=1234"
        print "Assuming a random input text:",text
    else:
        print "Input Port = ",sys.argv[1]
        text = " ".join(sys.argv[2:])
        print "Input Text = ",text
        port = int(sys.argv[1])
    local_http_req(text, port)
