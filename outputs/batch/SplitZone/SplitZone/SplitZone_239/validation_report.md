# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_239`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_239/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [191–205], lower_priority='Action_ZoneBlock' annotated_start=194, effective_Action_ZoneBlock_start=206.
> - Action 'Action_None' range [191-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [270-273] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [276-326] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [329-409] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [423-479] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 252, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [252-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-310] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-454] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [457-476] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-273] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-318] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-341] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-369] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [448-479] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-328] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-285] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-235] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [198-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-405] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-439] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-460] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-324] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-368] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-413] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '18' starts at frame 206, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [206-208] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-264] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-300] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-225] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [242-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-242] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [246-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-355] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [205-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [219-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-364] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [217-277] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-357] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-362] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-457] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-465] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-375] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-369] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-446] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-334] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-386] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-328] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-328] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [330-335] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-398] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-443] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-451] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-360] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-447] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [457-462] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-399] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-413] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-444] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-456] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-370] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-392] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-390] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-393] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-452] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [469-472] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-442] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-454] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-475] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-456] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-472] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [476-479] for track '40' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.