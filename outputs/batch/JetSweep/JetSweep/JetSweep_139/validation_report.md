# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_139`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_139/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [70–81], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=82.
> - Action 'Action_JetMotion' range [35-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [236-262] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [265-335] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-117] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-233] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-259] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-359] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [71-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-225] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [232-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-177] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-359] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-311] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-117] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-177] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-311] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-164] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-227] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-349] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-187] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-262] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-272] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-304] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-317] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-294] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-324] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-343] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-347] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '39' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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