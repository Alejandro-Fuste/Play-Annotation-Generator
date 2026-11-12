# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_95`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–65], lower_priority='Action_ZoneBlock' annotated_start=52, effective_Action_ZoneBlock_start=66.
> - Action 'Action_ZoneBlock' range [52-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [57-129] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-161] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-292] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-253] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-122] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [49-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 142, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [142-212] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-105] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-299] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-255] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '29' has 1 frames without a visible bounding box.
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