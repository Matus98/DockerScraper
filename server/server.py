from http.server import BaseHTTPRequestHandler

import psycopg2

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        page_data = get_data_from_db()
        if page_data != None:
            page_body = "<html lang="+"cs-cz"+"><body><meta charset="+"utf-8"+" /><div><table style="+'"margin: 0px auto;"'+">"
            for index,item in enumerate(page_data):
                if index %2==0:
                    page_body += f"<tr><td><img src={item[2]}><p style="+'"text-align:center;"'+f">{item[1]}</p></td>"
                else:
                    page_body += f"<td><img src={item[2]}><p style="+'"text-align:center;"'+f">{item[1]}</p></td></tr>"
            page_body += "</div></table></body></html>"
        else:
            page_body = "<html lang="+"cs-cz"+"><body><meta charset="+"utf-8"+" /><h1>Database is not loaded or empty</h1></body></html>"
        self.wfile.write(page_body.encode())


def get_data_from_db():
    mobile_records = []

    connection = psycopg2.connect(
        host="postgres",
        user="postgres",
        password="heslo123",
        dbname="postgres",
        port="5432",
    )
    cursor = connection.cursor()

    
    postgreSQL_select_Query = "SELECT * FROM public.flats LIMIT 500"

    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()

    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        return mobile_records
