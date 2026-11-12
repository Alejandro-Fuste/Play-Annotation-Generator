# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_194`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_194/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '2' (Unknown) duration 153 frames exceeds threshold 90 frames [start=247, end=399].
> - Segment 'Action_BallCarry' for track '3' has invalid range: start=245, end=243. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LG) duration 183 frames exceeds threshold 90 frames [start=217, end=399].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 183 frames exceeds threshold 90 frames [start=217, end=399].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [214–228], lower_priority='Action_ZoneBlock' annotated_start=217, effective_Action_ZoneBlock_start=229.
> - Action 'Action_None' range [214-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-244] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-331] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-312] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-372] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-400] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [247-291] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [294-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [301-305] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [310-374] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [380-386] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [388-399] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-435] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [217-243] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-271] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-334] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-387] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [217-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [296-313] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [317-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-444] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-312] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-341] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [345-353] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-449] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-379] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [255-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-320] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-378] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-386] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-409] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-420] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-277] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-313] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [217-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [232-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [244-254] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [261-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-431] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-216] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [217-317] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [320-345] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [349-366] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [376-390] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-406] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-90] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [214-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [229-266] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [272-280] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [283-287] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-372] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-388] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-449] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-396] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-303] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-310] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-321] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-366] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-389] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-313] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-421] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [333-439] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-443] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-382] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-437] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-370] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-395] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-382] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-423] for track '31' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.