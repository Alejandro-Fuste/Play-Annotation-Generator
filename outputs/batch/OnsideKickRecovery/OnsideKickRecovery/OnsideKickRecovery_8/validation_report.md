# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_8`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '20' has invalid range: start=116, end=109. Clamping end to start.
> - Action 'Action_None' range [2-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [65-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [96-140] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-125] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [95-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [110-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-13] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-43] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-53] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-69] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '32' has 1 frames without a visible bounding box.
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