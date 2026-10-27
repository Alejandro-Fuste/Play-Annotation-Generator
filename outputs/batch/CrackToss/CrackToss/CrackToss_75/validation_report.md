# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_75`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 152: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [55-196] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [55-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-170] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-133] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [58-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-89] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-191] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [58-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-172] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.