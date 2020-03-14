import camelot
from PyPDF2 import PdfFileReader as pdr


with open('data.pdf', 'rb') as pdf_obj:
    total_pages = pdr(pdf_obj).numPages
    '''
    print(total_pages)
    textpages = ""
    input1 = pdr(pdf_obj)
    for j in range(1,total_pages):
        print(j)
        xObject = input1.getPage(j)['/Resources']['/XObject'].getObject()
        print(xObject)
        for obj in xObject:
            print("inner loop running")
            if xObject[obj]['/Subtype'] != '/Image':
                textpages = textpages + "," + str(j)
                print(textpages)
    '''
    
    print("toatal pages in the PDF are: " + str(total_pages) + ".")
    for i in range(1,total_pages):
        print("scanning page " + str(i) + ".")
        tables = camelot.read_pdf("data.pdf", flavor = 'stream', pages = str(i), row_tol=10)
        if len(tables) > 0:
            print(str(len(tables)) + ' tables extracted on page'+ str(i)+".")
            tables.export('C:\\Users\\TEKINA\\Desktop\\pdf\\data'+str(i)+'.xlsx', f='excel')
                
            
        # print('table extracted on page '+ str(i)+ 'is: \n')
        # print(tables[0].df)
        # print(tables)
        #tables.export('C:\\Users\\TEKINA\\Desktop\\pdf\\data.xlsx', f='excel')
        # except:
            # pass


    #tables = camelot.read_pdf("data.pdf", flavor = 'stream') 
# pages ='28, 30'
# layout_kwargs={'detect_vertical': False}
# kind = ‘text’‘grid’‘contour’‘textedge’
# split_text=True
# edge_tol=500
# row_tol=10                 this may be solution to problem I want to solve
