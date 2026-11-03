# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_51`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [7–24], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=25.
> - Action 'Action_RunPostRoute' range [24-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-57] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-34] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-147] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-58] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-179] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [7-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-74] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-29] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-158] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-121] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-163] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.