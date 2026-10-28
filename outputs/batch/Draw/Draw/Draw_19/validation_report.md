# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_19`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [60–72], lower_priority='Action_PassBlock' annotated_start=63, effective_Action_PassBlock_start=73.
> - Action 'Action_None' range [60-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-98] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-104] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-228] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-94] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-238] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '31' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.