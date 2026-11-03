# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_43`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 44: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [1–13], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=14.
> - Action 'Action_BallCarry' range [83-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [199-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [219-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-56] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-55] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-187] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-54] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-97] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [12-26] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-57] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-163] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-215] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-219] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-130] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-139] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '33' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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