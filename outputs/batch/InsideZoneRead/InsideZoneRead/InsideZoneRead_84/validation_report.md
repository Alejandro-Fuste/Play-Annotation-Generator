# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_84`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_84/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [48–62], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=63.
> - Action 'Action_None' range [48-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-132] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-130] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [81-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [86-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [89-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-76] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-133] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '22' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.