# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_208`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_208/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [49–61], lower_priority='Action_ZoneBlock' annotated_start=51, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [49-137] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [199-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [204-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [49-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-197] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.