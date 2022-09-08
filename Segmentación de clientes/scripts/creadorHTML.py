from clases.razones import *
import codecs

def generate_html(clasic, gold, black):
    razones_clasic = [Razon(transaccion, clasic).razon for transaccion in clasic.cuenta.transacciones_r]
    razones_gold = [Razon(transaccion, gold).razon for transaccion in gold.cuenta.transacciones_r]
    razones_black = [Razon(transaccion, black).razon for transaccion in black.cuenta.transacciones_r]
    finish_html(clasic, generate_table_row(clasic, razones_clasic))
    finish_html(gold, generate_table_row(gold, razones_gold))
    finish_html(black, generate_table_row(black, razones_black))

def generate_table_row(client, razones):
    table_rows = ''
    for i in range(len(client.cuenta.transacciones_r)):
        table_rows += '<tr>'
        for key, value in client.cuenta.transacciones_r[i].items():
            if key in ['numero', 'fecha', 'tipo', 'estado', 'monto']:
                table_rows += f"<td>{value}</td>"

        table_rows += f"<td>{razones[i]}</td>"
        table_rows += '</tr>'
        table_rows += '<tr class="spacer"></tr>'

    return table_rows

def finish_html(client, table_rows):
    with codecs.open(f"{type(client).__name__}.html", "w", "utf-8") as file:
        html_content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css">
    <title>Reporte ITBANK</title>
  </head>
  <body>
  <div class="content">   
    <div class="container">
      <h1 class="mb-5">Reporte Transacciones - ITBANK</h1>
      <div class="container">
        <table class="table custom-table">
            <thead>
              <tr>  
                <th scope="col">Nombre</th>
                <th scope="col">Número</th>
                <th scope="col">DNI</th>
                <th scope="col">Dirección</th> 
              </tr>
            </thead>
            <tbody>
                <tr scope="row">
                  <td>{client.nombre}</td>
                  <td>{client.numero}</td>
                  <td>{client.dni}</td>
                  <td>{client.direccion.output_as_label()}</td>
                </tr>
            </table>
      </div>
      <div class="table-responsive custom-table-responsive">
        <table class="table custom-table">
            <h2 style="margin-top:20px;margin-bottom:20px" >Historial de Transacciones</h2>
            <h3>Cliente {type(client).__name__}</h2>
          <thead>
            <tr>  
              <th scope="col">Estado</th>
              <th scope="col">Tipo</th>
              <th scope="col">Monto</th>
              <th scope="col">Fecha</th>
              <th scope="col">Numero</th>
              <th scope="col">Razón Rechazo</th>
            </tr>
          </thead>
          <tbody>
            <tr scope="row">
              {table_rows}
            </tr>
            <tr class="spacer"></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  </body>
</html>
"""
        file.write(html_content)