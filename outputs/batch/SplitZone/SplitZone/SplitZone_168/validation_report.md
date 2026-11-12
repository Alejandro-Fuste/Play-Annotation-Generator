# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_168`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 179 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 338: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [150–162], lower_priority='Action_ZoneBlock' annotated_start=153, effective_Action_ZoneBlock_start=163.
> - Action 'Action_PreSnap' range [13-149] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-233] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-340] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-354] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-115] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [207-227] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-152] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-178] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-167] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '8' starts at frame 180, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [180-184] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-31] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 163, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [163-165] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [170-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-327] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-352] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-49] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-108] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [164-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-359] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-152] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-141] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '12' starts at frame 153, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [153-162] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [194-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [218-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-46] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-79] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-87] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-147] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [150-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [158-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [198-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [204-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-275] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-297] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-297] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-322] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-359] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-246] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-313] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-291] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-359] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-257] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-285] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-345] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-272] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-290] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-349] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-325] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-343] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-352] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-340] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-359] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-359] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-333] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-352] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '39' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.