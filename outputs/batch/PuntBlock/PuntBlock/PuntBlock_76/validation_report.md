# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_76`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 154: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '5' has invalid range: start=202, end=173. Clamping end to start.
> - Action 'Action_None' range [22-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [76-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-57] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-131] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-213] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [90-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-217] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-225] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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