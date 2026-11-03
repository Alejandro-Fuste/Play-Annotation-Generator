# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_11`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '9' has invalid range: start=189, end=188. Clamping end to start.
> - Action 'Action_None' range [9-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-184] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [104-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-164] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [179-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-88] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-99] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-70] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-210] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-132] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.