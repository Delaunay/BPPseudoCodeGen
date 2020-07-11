
from codegen.ue4_stub import *

from Script.FactoryGame import FGResourceSettings

class BP_ResourceSettings(FGResourceSettings):
    mResourceDepositTable = [{'DropChance': 15, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'MinAmount': 45, 'MaxAmount': 60, 'MiningAmount': 5}, {'DropChance': 10, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'MinAmount': 20, 'MaxAmount': 30, 'MiningAmount': 5}, {'DropChance': 8, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/OreCopper/Desc_OreCopper.Desc_OreCopper_C', 'MinAmount': 20, 'MaxAmount': 30, 'MiningAmount': 5}, {'DropChance': 7, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'MinAmount': 40, 'MaxAmount': 100, 'MiningAmount': 5}, {'DropChance': 17, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/OreGold/Desc_OreGold.Desc_OreGold_C', 'MinAmount': 15, 'MaxAmount': 30, 'MiningAmount': 5}, {'DropChance': 13, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'MinAmount': 15, 'MaxAmount': 30, 'MiningAmount': 5}, {'DropChance': 20, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'MinAmount': 10, 'MaxAmount': 20, 'MiningAmount': 5}, {'DropChance': 6, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'MinAmount': 20, 'MaxAmount': 75, 'MiningAmount': 5}, {'DropChance': 3, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/SAM/Desc_SAM.Desc_SAM_C', 'MinAmount': 30, 'MaxAmount': 60, 'MiningAmount': 2}, {'DropChance': 1, 'ResourceClass': '/Game/FactoryGame/Resource/RawResources/OreUranium/Desc_OreUranium.Desc_OreUranium_C', 'MinAmount': 50, 'MaxAmount': 60, 'MiningAmount': 5}]
    mResourceAmount = [{'Min': 1000, 'Max': 10000}, {'Min': 15000, 'Max': 30000}, {'Min': 40000, 'Max': 60000}]
    mPurityMultiplier = [0.5, 1, 2]
    mWaterResourceDescriptor = NewObject[Desc_Water]()
    mDefaultItemMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/DefaultItemMesh.DefaultItemMesh')
    mStackSizes = [{'Key': 1, 'Value': 'EStackSize::SS_ONE'}, {'Key': 500, 'Value': 'EStackSize::SS_HUGE'}, {'Key': 50, 'Value': 'EStackSize::SS_SMALL'}, {'Key': 100, 'Value': 'EStackSize::SS_MEDIUM'}, {'Key': 200, 'Value': 'EStackSize::SS_BIG'}, {'Key': 50000, 'Value': 'EStackSize::SS_FLUID'}]
    mItemDropClass = NewObject[BP_ItemPickup_Spawnable]()
    
