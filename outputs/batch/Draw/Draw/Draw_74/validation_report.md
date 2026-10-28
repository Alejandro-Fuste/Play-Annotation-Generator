# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_74`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [23–35], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=36.
> - Action 'Action_PassBlock' range [26-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [75-185] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-110] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-126] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '30' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.