# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_9`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 12: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [6–24], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=25.
> - Action 'Action_RunGoRoute' range [93-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [6-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-159] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-115] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-199] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [6-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-165] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-155] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-33] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-66] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-165] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-185] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [187-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [194-204] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [206-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-60] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-149] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-184] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-144] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-178] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '41' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.