# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_129`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 260: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [39-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-60] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-43] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-62] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-60] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-59] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [45-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-64] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-61] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-60] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-62] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [53-64] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '31' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.