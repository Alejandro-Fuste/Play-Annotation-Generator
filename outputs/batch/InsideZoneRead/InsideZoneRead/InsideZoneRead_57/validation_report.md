# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_57`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [62–74], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=75.
> - Action 'Action_None' range [62-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-206] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-199] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-172] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-92] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-114] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [116-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-135] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-123] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.