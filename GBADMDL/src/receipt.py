from dataclasses import dataclass

@dataclass
class Receipt:
    ''' Representação do nó de um recibo para um deputado '''
    bugged_date: str                            # "identify wether date had issues receipt_date: (datetime)"
    deputy_id: int                              # ID do deputado
    receipt_date: str                           # Data do recibo
    political_party: str                        # Partido do deputado
    state_code: str                             # Código do estado do deputado
    deputy_name: str                            # Nome do deputado
    receipt_social_security_number: float       # Número do seguro social (Nem sempre presente)
    receipt_description: str                    # Descrição do tipo de gasto
    establishment_name: str                     # Nome do estabelecimento favorecido
    receipt_value: int                          # Valor do recibo