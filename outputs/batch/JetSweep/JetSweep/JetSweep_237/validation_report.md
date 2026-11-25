# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_237`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_237/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '4' (TE) duration 141 frames exceeds threshold 90 frames [start=79, end=219].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RG) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [78–91], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=92.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 163 frames exceeds threshold 90 frames [start=79, end=241].
> - Action 'Action_BallCarry' range [103-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-211] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-231] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [240-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-243] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-199] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [79-215] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [218-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-296] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-318] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-127] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-224] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-196] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-116] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-260] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-241] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-255] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-267] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-177] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-298] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [300-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-199] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-311] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-312] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-266] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-291] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-305] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-294] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-302] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-313] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-326] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-311] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-307] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '43' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.