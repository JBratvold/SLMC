# Changes will only be applied to website from the "config.py" file
# Any changes made in "Daniel.py" will have to be copied and pasted into the "config.py" file 

# Individual's LP balance within Sacred Legend Mining Corporation:
# For example, if Sin Sacred owns 500k LP in the SLMC corp wallet, then set SinSacredLP = 500_000
SinSacredLP = 1_081_434
JupiterSacredLP = 0
PlutoSacredLP = 0   
DanielJoshLiquidationLP = 812_825

# ISK that our LP Broker owes the individual:
# For example, if the LP Broker owes Sin Sacred 2mil ISK, then set SinSacredISK = 2_000_000
SinSacredISK = 8_500_000_000
JupiterSacredISK = 0
PlutoSacredISK = 0

# System ID's
JITA_SYSTEM_ID = 30000142

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
CoreTemperatureRegulator = 57479
DreadGuristasCrystalTag = 17244
DreadGuristasGoldTag = 17248
CaldariCU1NexusChip = 17646
CaldariBY1NexusChip = 17647
CaldariAZ1NexusChip = 17643
EstamelTharchonsTag = 17295
MediumShieldExtenderI = 3829
SmallShieldExtenderI = 377
LargeShieldExtenderI = 3839
FederationNavyCommandSeargeantMajorInsigniaI = 15646
FederationNavyFleetMajorInsigniaI = 15593
FederationNavyFleetColonelInsigniaI = 15594
FederationNavyFleetColonelInsigniaII = 15673
CapBooster100 = 3554
CapBooster150 = 11283
CapBooster200 = 11285
CapBooster3200 = 41489
CapBooster400 = 11287
CapBooster50 = 264
CapBooster25 = 263
CapBooster75 = 3552
CapBooster800 = 11289
HornetI = 2464
VespaI = 15508
WardenI = 23559
WaspI = 1201

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
    57479: "Core Temperature Regulator",
    17244: "Dread Guristas Crystal Tag",
    17248: "Dread Guristas Gold Tag",
    17295: "Estamel Tharchon's Tag",
    17646: "Caldari CU-1 Nexus Chip",
    17647: "Caldari BY-1 Nexus Chip",
    17643: "Caldari AZ-1 Nexus Chip",
    3829: "Medium Shield Extender I",
    377: "Small Shield Extender I",
    3839: "Large Shield Extender I",
    15646: "Federation Navy Command Sergeant Major Insignia I",
    15593: "Federation Navy Fleet Major Insignia I",
    15594: "Federation Navy Fleet Colonel Insignia I",
    15673: "Federation Navy Fleet Colonel Insignia II",
    3554: "Cap Booster 100",
    11283: "Cap Booster 150",
    11285: "Cap Booster 200",
    41489: "Cap Booster 3200",
    11287: "Cap Booster 400",
    264: "Cap Booster 50",
    263: "Cap Booster 25",
    3552: "Cap Booster 75",
    11289: "Cap Booster 800",
    2464: "Hornet I",
    15508: "Vespa I",
    23559: "Warden I",
    1201: "Wasp I",
}


# Ship Blueprints
SHIP_BLUEPRINTS = {
    "Heron Navy Issue (ISK)": {
        "materials": {Tritanium: 32_000,
                      Pyerite: 6_000, 
                      Mexallon: 2_500,
                      Isogen: 500,
                      Nocxium: 30,
                      Zydrine: 20,
                      Megacyte: 10,
                      AutoIntegrityPreservationSeal: 10,
                      LifeSupportBackupUnit: 5},
        "flat_isk_cost": 2_000_000,
        "lp_cost": 4_000,
        "manufacturing_cost": 82_998,
    },
    "Heron Navy Issue (Tags)": {
        "materials": {Tritanium: 32_000,
                      Pyerite: 6_000, 
                      Mexallon: 2_500,
                      Isogen: 500,
                      Nocxium: 30,
                      Zydrine: 20,
                      Megacyte: 10,
                      DreadGuristasGoldTag: 1,
                      AutoIntegrityPreservationSeal: 10,
                      LifeSupportBackupUnit: 5},
        "flat_isk_cost": 0,
        "lp_cost": 4_000,
        "manufacturing_cost": 82_998,
    },
    "Heron Navy Issue (Chips)": {
        "materials": {Tritanium: 32_000,
                      Pyerite: 6_000, 
                      Mexallon: 2_500,
                      Isogen: 500,
                      Nocxium: 30,
                      Zydrine: 20,
                      Megacyte: 10,
                      CaldariBY1NexusChip: 4,
                      AutoIntegrityPreservationSeal: 10,
                      LifeSupportBackupUnit: 5},
        "flat_isk_cost": 0,
        "lp_cost": 4_000,
        "manufacturing_cost": 82_998,
    },
    "Cormorant Navy Issue (ISK)": {
        "materials": {Tritanium: 80_000,
                      Pyerite: 15_000, 
                      Mexallon: 5_000,
                      Isogen: 1_000,
                      Nocxium: 30,
                      Zydrine: 20,
                      Megacyte: 10,
                      AutoIntegrityPreservationSeal: 10,
                      LifeSupportBackupUnit: 5},
        "flat_isk_cost": 3_500_000,
        "lp_cost": 12_000,
        "manufacturing_cost": 146_714,
    },
    "Cormorant Navy Issue (Chips)": {
        "materials": {Tritanium: 80_000,
                      Pyerite: 15_000, 
                      Mexallon: 5_000,
                      Isogen: 1_000,
                      Nocxium: 30,
                      Zydrine: 20,
                      Megacyte: 10,
                      CaldariBY1NexusChip: 8,
                      AutoIntegrityPreservationSeal: 10,
                      LifeSupportBackupUnit: 5},
        "flat_isk_cost": 0,
        "lp_cost": 12_000,
        "manufacturing_cost": 146_714,
    },
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
    "Osprey Navy Issue (ISK)": {
        "materials": { Tritanium: 540_000,
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
    "Osprey Navy Issue (Tags)": {
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
    },
    "Osprey Navy Issue (Chips)": {
        "materials": { Tritanium: 540_000,
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
        "materials": { Tritanium: 2_800_000,
                      Pyerite: 1_000_000,
                      Mexallon: 180_000,
                      Isogen: 20_000,
                      Nocxium: 10_000,
                      Zydrine: 4_000,
                      Megacyte: 2_000,
                      AutoIntegrityPreservationSeal: 100,
                      LifeSupportBackupUnit: 50},
        "flat_isk_cost": 10_000_000,
        "lp_cost": 40_000,
        "manufacturing_cost": 7_734_558,
    },
    "Drake Navy Issue (Chips)": {
        "materials": { Tritanium: 2_800_000,
                      Pyerite: 1_000_000,
                      Mexallon: 180_000,
                      Isogen: 20_000,
                      Nocxium: 10_000,
                      Zydrine: 4_000,
                      Megacyte: 2_000,
                      CaldariCU1NexusChip: 5,
                      AutoIntegrityPreservationSeal: 100,
                      LifeSupportBackupUnit: 50},
        "flat_isk_cost": 0,
        "lp_cost": 40_000,
        "manufacturing_cost": 7_734_558,
    },
    "Ferox Navy Issue (ISK)": {
        "materials": { Tritanium: 2_800_000,
                      Pyerite: 1_000_000,
                      Mexallon: 180_000,
                      Isogen: 20_000,
                      Nocxium: 10_000,
                      Zydrine: 4_000,
                      Megacyte: 2_000,
                      AutoIntegrityPreservationSeal: 100,
                      LifeSupportBackupUnit: 50},
        "flat_isk_cost": 10_000_000,
        "lp_cost": 40_000,
        "manufacturing_cost": 7_734_558,
    },
    "Ferox Navy Issue (Chips)": {
        "materials": { Tritanium: 2_800_000,
                      Pyerite: 1_000_000,
                      Mexallon: 180_000,
                      Isogen: 20_000,
                      Nocxium: 10_000,
                      Zydrine: 4_000,
                      Megacyte: 2_000,
                      CaldariCU1NexusChip: 5,
                      AutoIntegrityPreservationSeal: 100,
                      LifeSupportBackupUnit: 50},
        "flat_isk_cost": 0,
        "lp_cost": 40_000,
        "manufacturing_cost": 7_734_558,
    },
    "Scorpion Navy Issue (ISK)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 20_000_000,
        "lp_cost": 100_000,
        "manufacturing_cost": 33_362_380,
    },
    "Scorpion Navy Issue (Tags)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      EstamelTharchonsTag: 1,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 0,
        "lp_cost": 100_000,
        "manufacturing_cost": 33_362_380,
    },
    "Scorpion Navy Issue (Chips)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      CaldariAZ1NexusChip: 2,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 0,
        "lp_cost": 100_000,
        "manufacturing_cost": 33_362_380,
    },
    "Raven Navy Issue (ISK)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 20_000_000,
        "lp_cost": 100_000,
        "manufacturing_cost": 999_999_999_999_999, # TODO FIND MANUFACTURING COST FOR THIS SHIP ------------------------------------------ 
    },
    "Raven Navy Issue (Tags)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      EstamelTharchonsTag: 1,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 0,
        "lp_cost": 100_000,
        "manufacturing_cost": 999_999_999_999_999, # TODO FIND MANUFACTURING COST FOR THIS SHIP ------------------------------------------ 
    },
    "Raven Navy Issue (Chips)": {
        "materials": { Tritanium: 8_000_000,
                      Pyerite: 4_000_000,
                      Mexallon: 600_000,
                      Isogen: 400_000,
                      Nocxium: 30_000,
                      Zydrine: 8_000,
                      Megacyte: 4_000,
                      CaldariAZ1NexusChip: 2,
                      AutoIntegrityPreservationSeal: 200,
                      CoreTemperatureRegulator: 1,
                      LifeSupportBackupUnit: 100},
        "flat_isk_cost": 0,
        "lp_cost": 100_000,
        "manufacturing_cost": 999_999_999_999_999, # TODO FIND MANUFACTURING COST FOR THIS SHIP ------------------------------------------ 
    },
    "Caldari Navy Medium Shield Extender (NoCraft)": {
        "materials": { MediumShieldExtenderI: 1,
                      FederationNavyFleetColonelInsigniaI: 2
                     },
        "flat_isk_cost": 2_000_000,
        "lp_cost": 3_000,
        "manufacturing_cost": 0,
    },
     "Caldari Navy Medium Shield Extender (Craft)": {
        "materials": { FederationNavyFleetColonelInsigniaI: 2,
                      Tritanium: 1_701,
                      Pyerite: 411,
                      Mexallon: 162,
                      Isogen: 6
                     },
        "flat_isk_cost": 2_000_000,
        "lp_cost": 3_000,
        "manufacturing_cost": 2_855,
     },
     "Caldari Navy Large Shield Extender (NoCraft)": {
         "materials": { LargeShieldExtenderI: 1,
                       FederationNavyFleetColonelInsigniaI: 2,
                       FederationNavyFleetColonelInsigniaII: 4
                      },
         "flat_isk_cost": 4_000_000,
         "lp_cost": 10_000,
         "manufacturing_cost": 0,
     }, 
     "Caldari Navy Large Shield Extender (Craft)": {
         "materials": { LargeShieldExtenderI: 1,
                       FederationNavyFleetColonelInsigniaI: 2,
                       FederationNavyFleetColonelInsigniaII: 4,
                       Tritanium: 3_383,
                       Pyerite: 2_769,
                       Mexallon: 181,
                      },
         "flat_isk_cost": 4_000_000,
         "lp_cost": 10_000,
         "manufacturing_cost": 999_999_999_999_999, # TODO FIND MANUFACTURING COST FOR THIS SHIP
     },
     "Caldari Navy Small Shield Extender (NoCraft)": {
         "materials": { SmallShieldExtenderI: 1,
                       FederationNavyCommandSeargeantMajorInsigniaI: 2,
                       FederationNavyFleetMajorInsigniaI: 4
                      },
         "flat_isk_cost": 500_000,
         "lp_cost": 1_000,
         "manufacturing_cost": 0
     },
    }
