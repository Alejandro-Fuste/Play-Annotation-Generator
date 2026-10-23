# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_2`
- **Input XML**: `output_showcase_final/SplitZone/SplitZone_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 92 frames exceeds threshold 90 frames [start=55, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 92 frames exceeds threshold 90 frames [start=55, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=55, end=146].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [52–67], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=68.
> - Action 'Action_None' range [52-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '6' starts at frame 97, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [97-209] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-114] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [52-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '23' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.