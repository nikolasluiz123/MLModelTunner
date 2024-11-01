from abc import ABC, abstractmethod
from typing import TypeVar

from scikit_learn.validator.results.common import ValidationResult

Result = TypeVar('Result', bound=ValidationResult)


class BaseValidator(ABC):
    """
    Classe base abstrata para validadores de modelos.

    Esta classe define a interface para os validadores de modelos de aprendizado de máquina,
    especificando métodos que devem ser implementados em subclasses. O validador pode
    incluir logs e configuração de paralelização.

    :param log_level: Nível de log para controle de saída de informações (padrão é 1).
    :param n_jobs: Número de trabalhos a serem executados em paralelo. -1 significa usar todos os processadores.
    """

    def __init__(self,
                 log_level: int = 1,
                 n_jobs: int = -1):
        """
        Inicializa um novo validador base.

        :param log_level: Nível de log para controle de saída de informações.
        :param n_jobs: Número de trabalhos a serem executados em paralelo.
        """
        self.log_level = log_level
        self.n_jobs = n_jobs

        self.start_best_model_validation = 0
        self.end_best_model_validation = 0

    @abstractmethod
    def validate(self,
                 searcher,
                 data_x,
                 data_y,
                 cv=None,
                 scoring=None) -> Result | None:
        """
        Função abstrata para validar um modelo.

        As subclasses devem implementar esta função para realizar a validação do modelo
        utilizando o buscador fornecido.

        :param searcher: Objeto responsável pela busca de hiperparâmetros ou pela seleção de modelos.
        :param data_x: Conjunto de dados de entrada (features) para validação.
        :param data_y: Conjunto de dados de saída (rótulos) para validação.
        :param cv: Estratégia de validação cruzada a ser utilizada (opcional).
        :param scoring: Métrica de avaliação a ser utilizada (opcional).

        :return: Um objeto do tipo Result contendo os resultados da validação ou None se não for aplicável.
        """
        ...
