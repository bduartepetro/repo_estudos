import xlsxwriter as opcoesDoXlsxWriter
import os 

nomeCaminhoArquivo = 'C:\\Users\\DPO1\\OneDrive - PETROBRAS\\Documentos\\0 - Estudos\\Udemy\\Python - Excel\\PrimeiroExemplo.xlsx' #acessando a pasta para executar/salvar o arquivo
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo) #Caminho com o nome do "workbook"
sheetPadrao = workbook.add_worksheet() #cria "sheet"

sheetPadrao.write("A1", "Nome") #escreve dentro da "sheet"
sheetPadrao.write("B1", "Idade") #escreve dentro da "sheet"
sheetPadrao.write("A2", "João") #escreve dentro da "sheet"
sheetPadrao.write("B2", 21) #escreve dentro da "sheet"
sheetPadrao.write("A3", "Jonas") #escreve dentro da "sheet"
sheetPadrao.write("B3", 56) #escreve dentro da "sheet"

workbook.close() #fecha arquivo para salvar o mesmo 

os.startfile(nomeCaminhoArquivo)