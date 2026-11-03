# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_10`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 22: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_BlockPunt' for track '4' has invalid range: start=60, end=59. Clamping end to start.
> - Action 'Action_PreSnap' range [0-51] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-157] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [48-102] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [111-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [120-138] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [141-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-13] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-24] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-12] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-101] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-64] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-59] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-84] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-145] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-91] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-189] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-180] for track '31' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.