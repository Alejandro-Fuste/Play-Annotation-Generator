# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_21`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 44: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '14' has invalid range: start=146, end=142. Clamping end to start.
> - Action 'Action_None' range [3-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [93-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [97-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [105-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [109-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [49-86] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-76] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [3-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '28' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.