# pylint: disable=missing-module-docstring
import asyncio

from viam.module.module import Module
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.services.vision import Vision

from src.re_id_tracker import ReIDObjetcTracker


async def main():
    """
    This function creates and starts a new module, after adding all desired
    resource models. Resource creators must be registered to the resource
    registry before the module adds the resource model.
    """
    Registry.register_resource_creator(
        Vision.SUBTYPE,
        ReIDObjetcTracker.MODEL,
        ResourceCreatorRegistration(
            ReIDObjetcTracker.new_service,
            ReIDObjetcTracker.validate_config,
        ),
    )
    module = Module.from_args()

    module.add_model_from_registry(Vision.SUBTYPE, ReIDObjetcTracker.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())