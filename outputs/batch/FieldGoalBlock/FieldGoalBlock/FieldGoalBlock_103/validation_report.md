# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_103`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 207: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [54-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-194] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-53] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 54, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [54-54] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-186] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-190] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-160] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-283] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '32' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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