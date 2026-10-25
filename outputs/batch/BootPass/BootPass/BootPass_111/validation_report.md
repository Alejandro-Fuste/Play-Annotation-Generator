# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_111`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_111/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_RunBlock' for track '13' has invalid range: start=82, end=32. Clamping end to start.
> - Segment 'Action_RunBlock' for track '15' has invalid range: start=82, end=63. Clamping end to start.
> - Segment 'Action_RunBlock' for track '17' has invalid range: start=82, end=30. Clamping end to start.
> - Action 'Action_None' range [15-193] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-192] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-217] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-217] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-234] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [15-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-217] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [15-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [24-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-68] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-59] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [82-197] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [199-206] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [209-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [216-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [220-223] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [230-237] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-194] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '28' has 1 frames without a visible bounding box.
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