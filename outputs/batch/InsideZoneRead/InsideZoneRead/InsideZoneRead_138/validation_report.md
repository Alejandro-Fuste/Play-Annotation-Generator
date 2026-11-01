# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_138`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_138/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 98 frames exceeds threshold 90 frames [start=175, end=272].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [172–183], lower_priority='Action_ZoneBlock' annotated_start=175, effective_Action_ZoneBlock_start=184.
> - Action 'Action_None' range [172-236] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-287] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-335] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [221-361] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-227] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-251] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-233] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [239-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [245-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-307] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-334] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-354] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-357] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-389] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-332] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-373] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [196-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-339] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-347] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-236] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-381] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [172-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-319] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-283] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-233] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-329] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' for track '20' starts at frame 217, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockSecondLevel' range [217-221] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [224-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [239-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [260-262] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-330] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-343] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-313] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-323] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-389] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-302] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-371] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-381] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-318] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-389] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-383] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [379-381] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '34' has 1 frames without a visible bounding box.
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