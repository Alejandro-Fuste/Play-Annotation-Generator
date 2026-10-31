# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_50`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [7–21], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=22.
> - Action 'Action_None' range [7-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-121] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-128] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-155] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [7-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-133] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-207] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-140] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-219] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-226] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-197] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.