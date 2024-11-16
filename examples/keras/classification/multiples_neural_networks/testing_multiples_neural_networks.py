from keras.src.callbacks import EarlyStopping, ReduceLROnPlateau

from examples.keras.classification.multiples_neural_networks.model_class import *
from examples.keras.classification.multiples_neural_networks.pre_processor import ExamplePreProcessor, input_shape, \
    batch_size, seed
from wrappers.keras.history_manager.classifier_history_manager import KerasClassifierHistoryManager
from wrappers.keras.hyper_params_search.hyper_band_searcher import KerasHyperBandSearcher
from wrappers.keras.process_manager.classifier_mult_process_manager import KerasClassifierMultProcessManager
from wrappers.keras.process_manager.pipeline import KerasPipeline
from wrappers.keras.validator.basic_classifier_validator import KerasBasicClassifierValidator

num_classes = 22

base_model = keras.applications.InceptionV3(
    include_top=False,
    weights='imagenet',
    input_shape=input_shape
)

pre_processor = ExamplePreProcessor()

early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)

validator = KerasBasicClassifierValidator(
    epochs=50,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr]
)

validator_6 = KerasBasicClassifierValidator(
    epochs=50,
    batch_size=64,
    log_level=1,
    callbacks=[early_stopping, reduce_lr]
)

validator_7 = KerasBasicClassifierValidator(
    epochs=50,
    batch_size=64,
    log_level=1,
    callbacks=[early_stopping, reduce_lr]
)


params_searcher_1 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_1',
    project_name='model_example_1',
    epochs=10,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_2 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_2',
    project_name='model_example_2',
    epochs=10,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_3 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_3',
    project_name='model_example_3',
    epochs=10,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_4 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_4',
    project_name='model_example_4',
    epochs=10,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_5 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_5',
    project_name='model_example_5',
    epochs=10,
    batch_size=batch_size,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_6 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_6',
    project_name='model_example_6',
    epochs=10,
    batch_size=64,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

params_searcher_7 = KerasHyperBandSearcher(
    objective='val_loss',
    directory='search_params_7',
    project_name='model_example_7',
    epochs=10,
    batch_size=64,
    log_level=1,
    callbacks=[early_stopping, reduce_lr],
    max_epochs=10,
    factor=3,
    hyper_band_iterations=1
)

history_manager_model_example_1 = KerasClassifierHistoryManager(output_directory='history_model_example_1',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_2 = KerasClassifierHistoryManager(output_directory='history_model_example_2',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_3 = KerasClassifierHistoryManager(output_directory='history_model_example_3',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_4 = KerasClassifierHistoryManager(output_directory='history_model_example_4',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_5 = KerasClassifierHistoryManager(output_directory='history_model_example_5',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_6 = KerasClassifierHistoryManager(output_directory='history_model_example_6',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

history_manager_model_example_7 = KerasClassifierHistoryManager(output_directory='history_model_example_7',
                                                                models_directory='models',
                                                                best_executions_file_name='best_executions')

pipelines = [
    KerasPipeline(
        model=ExampleKerasHyperModelV1(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        params_searcher=params_searcher_1,
        validator=validator,
        history_manager=history_manager_model_example_1
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV2(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        params_searcher=params_searcher_2,
        validator=validator,
        history_manager=history_manager_model_example_2
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV3(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        validator=validator,
        params_searcher=params_searcher_3,
        history_manager=history_manager_model_example_3
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV4(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        validator=validator,
        params_searcher=params_searcher_4,
        history_manager=history_manager_model_example_4
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV5(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        validator=validator,
        params_searcher=params_searcher_5,
        history_manager=history_manager_model_example_5
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV6(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        validator=validator_6,
        params_searcher=params_searcher_6,
        history_manager=history_manager_model_example_6
    ),
    KerasPipeline(
        model=ExampleKerasHyperModelV7(base_model=base_model, num_classes=num_classes),
        data_pre_processor=pre_processor,
        validator=validator_7,
        params_searcher=params_searcher_7,
        history_manager=history_manager_model_example_7
    )
]

history_manager_best_model = KerasClassifierHistoryManager(output_directory='best_executions',
                                                           models_directory='best_models',
                                                           best_executions_file_name='best_executions')
manager = KerasClassifierMultProcessManager(
    pipelines=pipelines,
    seed=seed,
    history_manager=history_manager_best_model,
    history_index=-1,
    save_history=True,
    delete_trials_after_execution=True
)

manager.process_pipelines()