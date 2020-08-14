import sys
sys.path.append("./")
import cgi
from http.server import BaseHTTPRequestHandler
import io
import json
from solver.mysolver import mySolver


slv = mySolver()

class csHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # get data from solver sql db
        message = json.dumps(slv.getoutput())
        # send header for json application
        self.send_response(200)
        self.send_header('Content-Type',
                         "application/json")
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

    def do_POST(self):
        # Parse the form posted data 
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # Begin the response
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )
        # print some data for client
        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['user-agent']))
        out.write('Path: {}\n'.format(self.path))
        out.write('Form data:\n')
        # run algo for what was posted in the form
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an json file
                file_data = field_item.file.read()
                file_len = len(file_data)
                slv.file = file_data
                # run algo for datas that are posted
                slv.run()

                out.write(
                    '\tUploaded {} as {!r} ({} bytes)\n'.format(
                        field, field_item.filename, file_len)
                )
                out.write("------------")
                out.write("Done!")
                out.write("------------\n")
            else:
                # Regular form value
                out.write('\t{}={}\n'.format(
                    field, form[field].value))

        # Disconnect our encoding wrapper
        out.detach()


