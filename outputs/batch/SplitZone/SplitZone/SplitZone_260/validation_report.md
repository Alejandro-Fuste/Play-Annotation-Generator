# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_260`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_260/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LT) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 112 frames exceeds threshold 90 frames [start=80, end=191].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=89.
> - Action 'Action_None' range [77-319] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-101] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [81-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-311] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [315-322] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [328-334] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-252] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-91] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-338] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-358] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-277] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-332] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-211] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-307] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-300] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-333] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-350] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '33' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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