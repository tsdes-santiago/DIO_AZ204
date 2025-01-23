import azure.functions as func
import logging

# Initialize the app
app = func.FunctionApp()

# Define the HTTP trigger function
@app.function_name(name="ValidateCPF")
@app.route(route="validate_cpf", auth_level=func.AuthLevel.ANONYMOUS)  # Defina o nível de autenticação aqui
def validate_cpf_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    # Get the CPF from the query string or request body
    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    # Validate the CPF
    if cpf:
        if validate_cpf(cpf):
            return func.HttpResponse(
                "CPF válido!",
                status_code=200
            )
        else:
            return func.HttpResponse(
                "CPF inválido!",
                status_code=200
            )
    else:
        return func.HttpResponse(
            "Por favor, forneça um CPF na query string ou no corpo da requisição.",
            status_code=400
        )

# Function to validate a CPF
def validate_cpf(cpf):
    # Remove any non-numeric characters from the CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Check if the CPF has the correct length
    if len(cpf) != 11:
        return False

    # Check if the CPF is all the same digit
    if cpf == cpf[0] * 11:
        return False

    # Calculate the first check digit
    soma1 = 0
    for i in range(9):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = 11 - (soma1 % 11)
    if resto1 == 10 or resto1 == 11:
        resto1 = 0
    if resto1 != int(cpf[9]):
        return False

    # Calculate the second check digit
    soma2 = 0
    for i in range(10):
        soma2 += int(cpf[i]) * (11 - i)
    resto2 = 11 - (soma2 % 11)
    if resto2 == 10 or resto2 == 11:
        resto2 = 0
    if resto2 != int(cpf[10]):
        return False

    # CPF is valid
    return True

