# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_161`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_161/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 539 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [313–325], lower_priority='Action_ZoneBlock' annotated_start=316, effective_Action_ZoneBlock_start=326.
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 96 frames exceeds threshold 90 frames [start=316, end=411].
> - Action 'Action_None' range [313-487] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-369] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-476] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-510] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-539] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-513] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-502] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-331] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-369] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-388] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [326-351] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [363-388] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-487] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [412-479] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-409] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-425] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [351-511] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-328] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [339-361] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [316-330] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [335-341] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [344-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [348-352] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-441] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-498] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-339] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-371] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-356] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-539] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-412] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-434] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-506] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-539] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-397] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-492] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-485] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-424] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-436] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-424] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-473] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-526] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-448] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-451] for track '34' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.