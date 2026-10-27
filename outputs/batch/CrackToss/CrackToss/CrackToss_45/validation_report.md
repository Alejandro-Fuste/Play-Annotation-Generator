# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_45`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '20' has invalid range: start=100, end=70. Clamping end to start.
> - Action 'Action_PullBlock' range [63-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-83] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-136] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-42] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-39] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [63-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [82-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '24' has 2 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.