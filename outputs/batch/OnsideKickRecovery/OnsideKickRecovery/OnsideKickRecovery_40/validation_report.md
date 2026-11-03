# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_40`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [3-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-36] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-81] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [28-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [69-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [89-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [103-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-120] for track '20' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [59-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '23' has 1 frames without a visible bounding box.
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