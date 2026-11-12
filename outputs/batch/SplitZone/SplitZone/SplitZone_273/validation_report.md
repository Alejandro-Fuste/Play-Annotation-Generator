# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_273`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_273/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [61–72], lower_priority='Action_ZoneBlock' annotated_start=69, effective_Action_ZoneBlock_start=73.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=69, end=64. Clamping end to start.
> - Action 'Action_None' range [61-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-202] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-295] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-76] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-289] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-100] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-157] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-280] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 119, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [119-121] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [111-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [123-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-131] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [64-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-53] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [76-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [85-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [104-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-257] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-297] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-90] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-284] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-274] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-336] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-338] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-353] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-293] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-301] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-306] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-268] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-304] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-300] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-359] for track '33' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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