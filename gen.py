import os
import csv
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

nameVar = '$VarName'
RGVar = '$VarRG'
sender_email = ""
context = ssl.create_default_context()
server =  smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)


subject = "Certificate"
body = "This is an email with attachment sent from Python"
receiver_email = ""


def subs(row, text):
    return text.replace(nameVar, row[0]).replace(RGVar, row[1])

def login():
    sender_email =input("Digite o email de pelo qual enviara:")
    password = input("Digite a senha do email:")
    server.login(sender_email, password)

def sendEmail(receiver_email, filename):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    message["To"] = receiver_email
    message["Bcc"] = receiver_email
    message.attach(MIMEText(body, "plain"))
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
    )
    message.attach(part)
    server.sendmail(sender_email, receiver_email, message.as_string())



if __name__ == '__main__':

    dirOutFile = input("digite o nome do Diretorio para o output:\n")

    if(os.path.exists("./"+dirOutFile+"_pdf")):
        os.system("rm ./"+dirOutFile+"_pdf/*")
    else:
        os.system("mkdir "+dirOutFile+"_pdf")

    if(os.path.exists("./"+dirOutFile+"_tex")):
        os.system("rm ./"+dirOutFile+"_tex/*")
    else:
        os.system("mkdir "+dirOutFile+"_tex")

    ifile = open('./listname/names.csv', 'r')
    reader = csv.reader(ifile)

    login()

    text = open('./template/cert.tex', 'r').read()

    for row in reader:
        outFileName = (row[0]+'.tex').replace(' ', '_');
        print(outFileName)
        cert = open(outFileName, 'w')
        cert.write(subs(row, text))
        cert.close()
        os.system("pdflatex " + outFileName)

        sendEmail(row[2], (row[0]+'.pdf').replace(' ', '_'))

    os.system("mv *.tex " + dirOutFile+"_tex/")
    os.system("mv *.pdf " + dirOutFile+"_pdf/")
    os.system("rm *.aux")
    os.system("rm *.log")
