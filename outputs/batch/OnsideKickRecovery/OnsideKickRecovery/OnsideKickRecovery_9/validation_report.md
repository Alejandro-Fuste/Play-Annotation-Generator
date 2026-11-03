# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OnsideKickRecovery_9`
- **Input XML**: `outputs/batch/OnsideKickRecovery/OnsideKickRecovery/OnsideKickRecovery_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OnsideKickRecovery.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureRecovery' for track '15' has invalid range: start=109, end=98. Clamping end to start.
> - Action 'Action_None' range [5-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-140] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-98] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_AttemptRecovery' range [96-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-23] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-37] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-31] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-118] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.