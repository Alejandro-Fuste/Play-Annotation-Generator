# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_184`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_184/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '2' has invalid range: start=168, end=158. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 162 frames exceeds threshold 90 frames [start=168, end=329].
> - Segment 'Action_SnapReceive' for track '5' has invalid range: start=165, end=132. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=168, end=121. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 162 frames exceeds threshold 90 frames [start=168, end=329].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [165–181], lower_priority='Action_ZoneBlock' annotated_start=168, effective_Action_ZoneBlock_start=182.
> - Segment 'Action_SplitBlock' for track '15' has invalid range: start=171, end=77. Clamping end to start.
> - Action 'Action_PreSnap' range [9-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [90-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-307] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-325] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-228] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-162] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-160] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-164] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-295] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-272] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-301] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-270] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-287] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-283] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-316] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-315] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.