# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_7`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 15: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '15' has invalid range: start=114, end=96. Clamping end to start.
> - Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-132] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-141] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [31-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [87-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-135] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-107] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-92] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-116] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '27' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.