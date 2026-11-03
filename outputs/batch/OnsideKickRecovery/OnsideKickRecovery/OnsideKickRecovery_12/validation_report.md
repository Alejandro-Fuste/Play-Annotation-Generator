# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_12`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 26: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '8' has invalid range: start=141, end=139. Clamping end to start.
> - Action 'Action_None' range [2-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-128] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-147] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-44] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [134-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-3] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-8] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-16] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-71] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-135] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_KickApproach' range [2-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [56-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-135] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-61] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-97] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [99-129] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [131-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-133] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.