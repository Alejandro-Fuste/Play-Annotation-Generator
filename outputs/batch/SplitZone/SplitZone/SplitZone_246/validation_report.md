# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_246`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_246/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 100 frames exceeds threshold 90 frames [start=98, end=197].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [95–110], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=111.
> - Action 'Action_ZoneBlock' range [98-184] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 198, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [198-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 198, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [198-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [99-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-299] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-173] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-299] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.