from abc import ABC

from wrappers.common.validator.results.common_validation_result import CommonValidationResult


class KerasValidationResult(CommonValidationResult, ABC):

    def __init__(self, model, history: dict):
        self.model = model
        self.history = history
