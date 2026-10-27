# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_176`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_176/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 353: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [10-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [12-30] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [34-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [12-43] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [46-60] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-160] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-107] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-96] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-166] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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