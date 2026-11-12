# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_10`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [57–66], lower_priority='Action_ZoneBlock' annotated_start=60, effective_Action_ZoneBlock_start=67.
> - Segment 'Action_Handoff' for track '17' has invalid range: start=93, end=66. Clamping end to start.
> - Action 'Action_None' range [57-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-219] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [115-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-251] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [253-287] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-162] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-195] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [65-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [72-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-99] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [57-66] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-255] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-292] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-190] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-211] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-293] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.