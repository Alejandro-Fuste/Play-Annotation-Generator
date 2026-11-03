# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_79`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [15–30], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=31.
> - Action 'Action_None' range [15-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-78] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [31-43] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-93] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-102] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-130] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-212] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '31' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '35' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.