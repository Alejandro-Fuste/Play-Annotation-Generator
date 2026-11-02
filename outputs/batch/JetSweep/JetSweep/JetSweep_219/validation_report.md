# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_219`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [81–89], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=90.
> - Action 'Action_None' range [81-233] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [100-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [191-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-227] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-103] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-227] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-96] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [82-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [81-89] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-156] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-246] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-247] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-263] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '31' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.