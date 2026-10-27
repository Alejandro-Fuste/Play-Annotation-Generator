# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_74`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_74/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 150: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_DownBlock' for track '4' has invalid range: start=35, end=29. Clamping end to start.
> - Segment 'Action_DownBlock' for track '5' has invalid range: start=35, end=26. Clamping end to start.
> - Segment 'Action_DownBlock' for track '6' has invalid range: start=35, end=29. Clamping end to start.
> - Segment 'Action_PullBlock' for track '9' has invalid range: start=35, end=29. Clamping end to start.
> - Segment 'Action_BallCarry' for track '9' has invalid range: start=66, end=29. Clamping end to start.
> - Segment 'Action_PullLeadBlock' for track '10' has invalid range: start=35, end=19. Clamping end to start.
> - Segment 'Action_BallSnap' for track '14' has invalid range: start=27, end=19. Clamping end to start.
> - Action 'Action_PreSnap' range [0-20] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-29] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-19] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [27-29] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-24] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-228] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-348] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-361] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-321] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-276] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-321] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-335] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-248] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [69-287] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-286] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-281] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-264] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-270] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-326] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [328-387] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-240] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-340] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [69-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-221] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-419] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-225] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-290] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-405] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-241] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-419] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-242] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-286] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-304] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-334] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-351] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-392] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-306] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-347] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-367] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-410] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-264] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-330] for track '36' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [267-277] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-419] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-419] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-321] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-391] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-382] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-346] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-375] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-383] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-405] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-413] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-390] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-410] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-416] for track '50' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.