# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_20`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [15–28], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=29.
> - Action 'Action_None' range [15-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-124] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [28-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-191] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-113] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-129] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [142-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [183-207] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-24] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-49] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-56] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '27' has 3 frames without a visible bounding box.
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