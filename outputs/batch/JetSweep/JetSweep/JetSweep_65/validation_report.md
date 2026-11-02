# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_65`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 132: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '20' has invalid range: start=220, end=197. Clamping end to start.
> - Action 'Action_None' range [189-223] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-202] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-294] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-288] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-196] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-205] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [207-228] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [237-244] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-351] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-212] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-281] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-273] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-226] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-310] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [194-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-37] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-251] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-337] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-148] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-278] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-290] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-302] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-318] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-228] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [238-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [218-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [253-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-336] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-347] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-257] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-275] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-334] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-359] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-359] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-358] for track '34' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.