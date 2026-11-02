# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_89`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 124 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [76–86], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=87.
> - Action 'Action_None' range [76-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-229] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-109] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-128] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-266] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [110-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [90-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-282] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-328] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-133] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-209] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-149] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-219] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-293] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [80-95] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [91-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-189] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-250] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-153] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-329] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-213] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-271] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-314] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-315] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-291] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-314] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.