# Mineral IDs
Tritanium = 34
Pyerite = 35
Mexallon = 36
Isogen = 37
Nocxium = 38
Zydrine = 39
Megacyte = 40
Pyroxeres = 1224

# Component ID's
AutoIntegrityPreservationSeal = 57478
LifeSupportBackupUnit = 57486
DreadGuristasCrystalTag = 17244
CaldariCU1NexusChip = 17646

TYPE_NAMES = {
    34: "Tritanium",
    35: "Pyerite",
    36: "Mexallon",
    37: "Isogen",
    38: "Nocxium",
    39: "Zydrine",
    40: "Megacyte",
    1224: "Pyroxeres",
    57478: "Auto Integrity Preservation Seal",
    57486: "Life Support Backup Unit",
    17244: "Dread Guristas Crystal Tag",
    17646: "Caldari CU-1 Nexus Chip",
}


# Ship Blueprints
SHIP_BLUEPRINTS = {
    "Caracal Navy Issue (ISK)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 5_000_000,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
    "Caracal Navy Issue (Tags)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      DreadGuristasCrystalTag: 1,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 0,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
    "Caracal Navy Issue (Chips)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      CaldariCU1NexusChip: 4,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 0,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
    "Drake Navy Issue (ISK)": {
        "materials": { Tritanium: 2_800_000
                      Pyerite: 1_000_000
                      Mexallon: 180_00
                      Isogen: 20_000
                      Nocxium: 10_000
                      Zydrine: 4_000
                      Megacyte: 2_000
                      AutoIntegrityPreservationSeal: 100
                      LifeSupportBackUnit: 50},
        "flat_isk_cost": 10_000_000,
        "manufacturing_cost": 7_734_558,
    },
    "Ferox Navy Issue (ISK)": {
        "materials": { Tritanium: 2_800_000
                      Pyerite: 1_000_000
                      Mexallon: 180_00
                      Isogen: 20_000
                      Nocxium: 10_000
                      Zydrine: 4_000
                      Megacyte: 2_000
                      AutoIntegrityPreservationSeal: 100
                      LifeSupportBackUnit: 50},
        "flat_isk_cost": 10_000_000,
        "manufacturing_cost": 7_734_558,
    },
    "Osprey Navy Issue (Tags)" {
        "materials": { Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      DreadGuristasCrystalTag: 1,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 0,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
}
