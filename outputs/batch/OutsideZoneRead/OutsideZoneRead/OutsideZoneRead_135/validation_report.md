# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_135`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_135/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 95 frames exceeds threshold 90 frames [start=11, end=105].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 95 frames exceeds threshold 90 frames [start=11, end=105].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [8–23], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=24.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 95 frames exceeds threshold 90 frames [start=11, end=105].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 95 frames exceeds threshold 90 frames [start=11, end=105].
> - Action 'Action_None' range [8-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-98] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-143] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-219] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-46] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-99] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-130] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.