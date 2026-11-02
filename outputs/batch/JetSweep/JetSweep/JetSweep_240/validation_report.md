# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_240`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_240/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [117–126], lower_priority='Action_ZoneBlock' annotated_start=119, effective_Action_ZoneBlock_start=127.
> - Action 'Action_PreSnap' range [0-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-130] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-252] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-281] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-213] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-170] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-267] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [119-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [25-34] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [42-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [49-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [56-64] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [69-122] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [127-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [131-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-159] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-197] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-220] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-308] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-254] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-311] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-250] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-266] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-279] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-304] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-260] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-272] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-297] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-329] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-286] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-298] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '45' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.